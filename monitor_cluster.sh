#!/bin/bash

while read line; do
    ssh -t $line "
    nohup python ~/sverma11/Monitoring/monitor.py ~/sverma11/Monitoring/LOGS/LOG_$(date -u +%F_%T).csv &
    sleep 0.1
    cat /tmp/monitor_pid.txt
    " < /dev/null &
done < ~/machines
sleep 1 && $@ && sleep 2
while read line; do
    ssh -t $line "
    echo \"kill \$(cat /tmp/monitor_pid.txt)\"
    kill \$(cat /tmp/monitor_pid.txt)
    " < /dev/null &
done < ~/machines
