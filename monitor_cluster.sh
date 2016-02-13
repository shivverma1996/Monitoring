#!/bin/bash

while read line; do
    ssh -t $line "
    nohup python /proj/ISS/powerGraph-exp/monitor.py > /graphlab/LOG_$(date -u +%F_%T).txt &
    sleep 0.1
    cat /tmp/monitor_pid.txt
    " < /dev/null
done < ~/machines
$@
while read line; do
    ssh -t $line "
    echo \"kill \$(cat /tmp/monitor_pid.txt)\"
    kill \$(cat /tmp/monitor_pid.txt)
    " < /dev/null &
done < ~/machines
