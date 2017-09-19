#!/bin/bash

export PATH=/opt/java/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

PROJECT_NAME=devicehive
PROJECT_PATH=/opt/webapps/${PROJECT_NAME}/current
PROJECT_LOG_PATH=/data/logs/webapps/${PROJECT_NAME}

PID_KEY=${PROJECT_PATH}/'[d]evicehive.jar'

SYSTEM_VARIABLES="-Dspring.config.location=${PROJECT_PATH}/conf/"

do_start() {
        PID=$(ps aux | grep "${PID_KEY}" | awk '{print $2}')
        if [ -z "$PID" ];then
                if [ ! -d ${PROJECT_LOG_PATH} ];then
                        mkdir -p ${PROJECT_LOG_PATH}
                fi

                if [ -f "${PROJECT_PATH}/conf/logback.xml" ];then
                        SYSTEM_VARIABLES="${SYSTEM_VARIABLES} -Dlogging.config=${PROJECT_PATH}/conf/logback.xml"
                fi

                echo "Service is starting ..."
                java ${SYSTEM_VARIABLES} -jar ${PROJECT_PATH}/devicehive.jar > ${PROJECT_LOG_PATH}/startup.log 2>&1 &
                sleep 2
                echo OK > /dev/null &
                echo "Service is up!"
        else
                echo "Service is running"
        fi
}

do_stop() {
        PID=$(ps aux | grep "${PID_KEY}" | awk '{print $2}')
        if [ -z "$PID" ];then
                echo "Service is not running"
        else
                echo "Service is shutting ... "
                kill -s SIGTERM $PID
                echo "Service is down!"
        fi
}

do_restart() {
        do_stop
        sleep 5
        do_start
}

do_status() {
        PID=$(ps aux | grep "${PID_KEY}" | awk '{print $2}')
        if [ -z "$PID" ];then
                echo "Service is not running"
        else
                echo "Service is running"
        fi
}

case $1 in
        start)
                do_start
                ;;
        stop)
                do_stop
                ;;
        restart)
                do_restart
                ;;
        status)
                do_status
                ;;
        *)
                echo "Usage: $0 {start|stop|restart|status}"
                exit 0
                ;;
esac

