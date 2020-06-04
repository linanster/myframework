# coding:utf8
#
from threading import Lock
from flask import Flask, render_template, session, request, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
import subprocess

async_mode = None

app_myframework_logmonitor = Flask(__name__, template_folder='.')
app_myframework_logmonitor.config['SECRET_KEY'] = 'secret!'
app_myframework_logmonitor.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
socketio = SocketIO(app_myframework_logmonitor, async_mode=async_mode)
thread = None
thread_lock = Lock()

def watch_log():
    # logfile = os.path.join(logfolder, 'log_module1.txt')
    logfile = '/git/myframework/logs/log_module1.txt'
    p = subprocess.Popen("tail -f {}".format(logfile), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = p.stdout.readline().decode('utf-8')[0:-1]
        socketio.emit('mylog', output, namespace='/test', broadcast=True)

@app_myframework_logmonitor.route('/')
@app_myframework_logmonitor.route('/index')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(watch_log)
    # emit('test', {'data': 'Connected', 'count': 0})
    socketio.emit('mylog', 'Connected!', namespace='/test', broadcast=True)

