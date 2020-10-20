from flask import Blueprint, request, render_template, flash, redirect, url_for, g
import os

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running
from app.lib.socketioutils import send_msg_hello
from app.views.blue_main import blue_main

from flask_login import login_required, fresh_login_required
from app.lib.myauth import my_page_permission_required

from app.myglobals import ROLES

blue_test = Blueprint('blue_test', __name__, url_prefix='/test')

@blue_test.route('/')
@blue_test.route('/index')
@viewfunclog
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
    return render_template('test_test2.html')

@blue_test.route('/test4')
@viewfunclog
def vf_test4():
    return render_template('test_test4.html')

@blue_test.route('/test5')
@viewfunclog
def vf_test5():
    return render_template('test_test5.html')

@blue_test.route('/test6')
@viewfunclog
def vf_test6():
    return render_template('test_test6.html')

@blue_test.route('/login')
@login_required
@viewfunclog
def vf_login():
    return "Login success"

@blue_test.route('/freshlogin')
@fresh_login_required
@viewfunclog
def vf_freshlogin():
    return "Fresh Login success"

@blue_test.route('/permission1')
@login_required
@my_page_permission_required(ROLES.VIEW)
@viewfunclog
def vf_permission1():
    return render_template('test_permission1.html')

@blue_test.route('/permission2')
@login_required
@my_page_permission_required(ROLES.ADMIN)
@viewfunclog
def vf_permission2():
    return render_template('test_permission2.html')
