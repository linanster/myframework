from flask_socketio import SocketIO
from threading import Lock
import subprocess
import time, os

from app.myglobals import logfolder, LOG_MONITOR_ENABLE
from app.lib.mydecorator import threadmaker

socketio = SocketIO()

thread1 = None
thread2 = None
thread_lock1 = Lock()
thread_lock2 = Lock()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_background', {'data': 'Server generated event', 'count': count}, namespace='/test')

def watch_log():
    logfile = os.path.join(logfolder, 'log_module1.txt')
    p = subprocess.Popen("tail -f {}".format(logfile), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = p.stdout.readline().decode('utf-8')[0:-1]
        socketio.emit('my_log', output, namespace='/test', broadcast=True)


@socketio.on('connect', namespace='/test')
def socket_connect():
    time.sleep(1)
    # 1. echo 'Connected'
    msg = 'Connected!'
    socketio.emit('my_msg', msg, namespace='/test')
    # 2. background thread1
    global thread1
    with thread_lock1:
        if thread1 is None:
            socketio.emit('my_background', {'data': 'Start background thread', 'count': 0}, namespace='/test')
            thread1 = socketio.start_background_task(background_thread)
    # 3. background thread2
    if not LOG_MONITOR_ENABLE:
        return
    global thread2
    with thread_lock2:
        if thread2 is None:
            socketio.emit('my_log', 'Start watch log', namespace='/test')
            thread2 = socketio.start_background_task(watch_log)


