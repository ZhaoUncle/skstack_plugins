#!/bin/bash
# this script have been used for sprintboot service status check
AppSpringName=$1
#waiting for App startup
sleep 10s
for(( i=1; i<=24;i++ ))
    do
        hostname=`hostname`
        AppInstance=`curl -s "http://eureka.mitrade.cloud:9001" |grep $hostname:$AppSpringName:|awk -F / '{print $3}'`
        status=`curl -s http://$AppInstance/health/status`
        if [ -n "$status" ];then
            if [ $status -eq 1 ];then
                echo successful;
                exit 0;
            fi

        fi
        sleep 5s
    done
echo "failed"
exit 1
