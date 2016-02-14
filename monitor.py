import psutil
from sys import argv, exit
from time import gmtime, strftime
from os import getpid, getppid
import signal
import csv

def sigterm_handler(_signo, _stack_frame):
    exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

pid = getpid()
f = open('/tmp/monitor_pid.txt', 'w')
f.write(str(pid) + "\n")
f.close()

with open(argv[1],'w') as csvfile:
    network_fieldnames=['bytes_sent','bytes_recv','packets_sent','packets_recv']
    fieldnames = ['current_time','cpu_percent_per_cpu','memory_percent'] + map(lambda x : 'net_io_'+x, network_fieldnames)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    net_tot_before = psutil.net_io_counters()
    while True:
        line = {}
        line['current_time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        line['cpu_percent_per_cpu'] = str(psutil.cpu_percent(interval=1, percpu=True))
        line['memory_percent'] = str(psutil.virtual_memory().percent)
        net_tot_now = psutil.net_io_counters()
        for idx, field in enumerate(network_fieldnames):
            line['net_io_'+field] = str(net_tot_now[idx] - net_tot_before[idx])
        writer.writerow(line)
