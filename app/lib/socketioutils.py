from app.ext.mysocketio import socketio
import time

from app.lib.mydecorator import processmaker, threadmaker


@threadmaker
def watch_log():
    pass

@threadmaker
def send_msg():
    time.sleep(1)
    for i in range(1, 6):
        msg = 'hello, %d' % i
        # socketio.emit('mylog', msg, namespace='/test', broadcast=True)
        socketio.emit('mymsg', msg, namespace='/test', broadcast=True)
        time.sleep(1)
    msg = 'done'
    # socketio.emit('mylog', msg, namespace='/test', broadcast=True)
    socketio.emit('mymsg', msg, namespace='/test', broadcast=True)

