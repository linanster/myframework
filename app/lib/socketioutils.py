from app.ext.mysocketio import socketio
import time

from app.lib.mydecorator import processmaker, threadmaker


@threadmaker
def send_msg_hello():
    time.sleep(1)
    for i in range(1, 6):
        msg = 'hello, %d' % i
        socketio.emit('mymsg', msg, namespace='/test', broadcast=True)
        time.sleep(1)
    msg = 'done'
    socketio.emit('mymsg', msg, namespace='/test', broadcast=True)

