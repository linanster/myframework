#!/usr/bin/env bash
#
set -o errexit

if [ $# -eq 0 ]; then
    echo "run.sh [--start] [--stop] [--status] [--init]"
    exit 1
fi
if [ "$1" != "--start" -a "$1" != "--stop" -a "$1" != "--status" -a "$1" != "--init" ]; then
    echo "run.sh [--start] [--stop] [--status] [--init]"
    exit 1
fi

workdir=$(cd "$(dirname $0)" && pwd)
cd "$workdir"

if [ "$1" == "--init" ]; then
    pip3 install virtualenv
    virtualenv venv
    source ./venv/bin/activate
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "==init config complete=="
        exit 0
    else
        echo "==init config fail=="
        exit 1
    fi
fi

if [ -d venv ]; then
    source ./venv/bin/activate
else
    echo "==venv error=="
    exit 1
fi

# cd "$workdir/app"

if [ "$1" == '--start' ]; then
    echo "gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework"
    # todo --daemon
    # todo --user user1 --group user1
    if [ "$2" == '--nodaemon' ]; then
        gunicorn --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
    else
        gunicorn --daemon --workers 1 --bind 0.0.0.0:4000 --timeout 300 --worker-class eventlet wsgi:application_framework
    fi
    ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}'
    exit 0
fi

if [ "$1" == "--stop" ]; then
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    if [ "$pid" == "" ]; then
        echo "not running" 
    else
        echo "kill $pid"
        kill "$pid"
    fi
    exit 0
fi

if [ "$1" == "--status" ]; then
    pid=$(ps -ef | fgrep "gunicorn" | grep "application_framework" | awk '{if($3==1) print $2}')
    echo "$pid"
    if [ "$pid" == "" ]; then
        echo "stopped" 
    else
        echo "started"
    fi
    exit 0
fi

