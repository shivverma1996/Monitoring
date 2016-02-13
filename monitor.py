import psutil
from sys import argv, exit
from time import gmtime, strftime
from os import getpid, getppid
import signal

def sigterm_handler(_signo, _stack_frame):
    print("received sigterm")
    exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

pid = getpid()
f = open('/tmp/monitor_pid.txt', 'w')
f.write(str(pid) + "\n")
f.close()

while True:
    line = ""
    line += strftime("%Y-%m-%d %H:%M:%S", gmtime())
    line += " " + str(psutil.cpu_percent(interval=1, percpu=True))
    line += " " + str(psutil.virtual_memory().percent) + "%"
    print(line)
