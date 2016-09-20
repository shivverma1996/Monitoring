#!/bin/bash

#while read line; do
#    ssh -t $line "
#    sudo ntpd -q;
#    nohup python ~/sverma11/Monitoring/monitor.py ~/sverma11/LOGS/LOG_$(date -u +%F_%T).csv &
#    sleep 0.1
#    cat /tmp/monitor_pid.txt
#    " < /dev/null &
#done < ~/sverma11/machines9
#sleep 1 && $@ && sleep 2
while read line; do
    ssh -t $line "
	ps -aef | grep monitor.py | cut -d' ' -f5 | xargs kill -9
    " < /dev/null
done < ~/machines
