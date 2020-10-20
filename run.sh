#!/usr/bin/env bash
#
# set -o errexit

# 1.variables definition

usage=$"
Usage: run.sh [--start [--ssl --nodaemon]] [--stop] [--status] [--init]
              [--logmonitor --start/--stop/--status]
"
workdir=$(cd "$(dirname $0)" && pwd)

# 2.functions definition

function activate_venv() {
    if [ -d venv ]; then
        source ./venv/bin/activate || source ./venv/Script/activate
    else
        echo "==venv error=="
    exit 1
    fi
}


function run_init(){
    pip3 install virtualenv
    virtualenv venv
    source ./venv/bin/activate
    # pip3 install -r requirements.txt
    pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    if [ $? -eq 0 ]; then
        echo "==init config complete=="
        exit 0
    else
        echo "==init config fail=="
        exit 1
    fi
}


function run_start_legacy(){
    activate_venv
    if [ "$1" == '--nodaemon' ]; then
        gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
        echo "gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework"
    elif [ "$1" == '' ]; then
        gunicorn --daemon --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
        echo 'gunicorn --daemon --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework'
    else
        echo 'wrong options!'
        exit 1
    fi
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    echo "$pid"
    exit 0
}

function run_start(){
    activate_venv
    case "$1$2" in
        "")
            gunicorn --daemon --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
            echo 'gunicorn --daemon --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework'
            ;;
        "--nodaemon")
            gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
            echo "gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework"
            ;;
        "--ssl")
            gunicorn --daemon --workers 1 --bind 0.0.0.0:4001 --keyfile ./cert/server.key --certfile ./cert/server.cert --timeout 300 --worker-class eventlet wsgi:application_framework
            echo 'gunicorn --daemon --workers 1 --bind 0.0.0.0:4001 --keyfile ./cert/server.key --certfile ./cert/server.cert --timeout 300 --worker-class eventlet wsgi:application_framework'
            ;;
        "--ssl--nodaemon")
            gunicorn --workers 1 --bind 0.0.0.0:4001 --keyfile ./cert/server.key --certfile ./cert/server.cert --timeout 300 --worker-class eventlet wsgi:application_framework
            echo 'gunicorn --workers 1 --bind 0.0.0.0:4001 --keyfile ./cert/server.key --certfile ./cert/server.cert --timeout 300 --worker-class eventlet wsgi:application_framework'
            ;;
        *)
            echo 'wrong options!'
            exit 1
    esac
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    echo "$pid"
    exit 0
}

function run_status(){
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    echo "$pid"
    if [ "$pid" == "" ]; then
        echo "stopped"
    else
        echo "started"
    fi
    exit 0
}

function run_stop(){
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    echo "$pid"
    if [ "$pid" == "" ]; then
        echo "not running"
    else
        echo "kill $pid"
        kill "$pid"
    fi
    exit 0
}

function run_logmonitor(){
    if [ "$1" == "--start" ]; then
        activate_venv
        cd logmonitor
        if [ "$2" == '--nodaemon' ]; then
            gunicorn --workers 1 --bind 0.0.0.0:4001 --timeout 300 --worker-class eventlet app:app_myframework_logmonitor
            echo "gunicorn --workers 1 --bind 0.0.0.0:4001 --timeout 300 --worker-class eventlet app:app_myframework_logmonitor"
        else
            gunicorn --daemon --workers 1 --bind 0.0.0.0:4001 --timeout 300 --worker-class eventlet app:app_myframework_logmonitor
            echo "gunicorn --daemon --workers 1 --bind 0.0.0.0:4001 --timeout 300 --worker-class eventlet app:app_myframework_logmonitor"
        fi
        pid=$(ps -ef | fgrep "gunicorn" | grep "app_myframework_logmonitor" | awk '{if($3==1) print $2}')
        echo "$pid"
    elif [ "$1" == "--stop" ]; then
        pid=$(ps -ef | fgrep "gunicorn" | grep "app_myframework_logmonitor" | awk '{if($3==1) print $2}')
        echo "$pid"
        if [ "$pid" == "" ]; then
            echo "not running"
        else
            echo "kill $pid"
            kill "$pid"
        fi
    elif [ "$1" == "--status" ]; then
        pid=$(ps -ef | fgrep "gunicorn" | grep "app_myframework_logmonitor" | awk '{if($3==1) print $2}')
        echo "$pid"
        if [ "$pid" == "" ]; then
            echo "stopped"
        else
            echo "started"
        fi
    else
        echo "${usage}"
    fi
    exit 0

}

# 3.start code

cd "$workdir"

if [ $# -eq 0 ]; then
    echo "${usage}"
    exit 1
fi

if [ $# -ge 1 ]; then
  case $1 in
    --help|-h)
        echo "$usage"
        exit 0
        ;;
    --init)
        run_init
        ;;
    --start)
        run_start $2 $3
        ;;
    --status)
        run_status
        ;;
    --stop)
        run_stop
        ;;
    --logmonitor)
        run_logmonitor $2 $3
        ;;
    *)
        echo "$usage"
        exit 1
        ;;
  esac
fi

