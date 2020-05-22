from flask import Blueprint, request, render_template, flash, redirect, url_for
import os

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running

from app.lib.socketioutils import watch_log, send_msg

blue_test = Blueprint('blue_test', __name__, url_prefix='/test')

@blue_test.route('/')
@blue_test.route('/index')
def vf_index():
    return render_template('test_index.html')


@blue_test.route('/test1')
@viewfunclog
def vf_test1():
    status = get_running()
    return render_template('test_test1.html', status=status)

@blue_test.route('/test2')
@viewfunclog
def vf_test2():
    watch_log()
    send_msg()
    return render_template('test_test2.html')

