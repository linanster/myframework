from flask import Blueprint, request, render_template, flash, redirect, url_for, g
import os
from flask_login import login_user, logout_user

from app.models.sqlite import User
from app.lib.mydecorator import viewfunclog
from app.lib.mylogger import logger_module1
from app.views.blue_main import blue_main


blue_auth = Blueprint('blue_auth', __name__, url_prefix='/auth')

@blue_auth.route('/login', methods=['GET', 'POST'])
@viewfunclog
def login():
    logger_module1.warn('client login from {}'.format(request.remote_addr))
    # 1. GET method, 进入登录页面
    if request.method == 'GET':
        # 1.1 http://10.30.30.101:4000/auth/login, next_page为None
        # 1.2 http://10.30.30.101:4000/auth/login?next=%2Fadmin%2Findex, next_page为/admin/index
        next_page = request.args.get('next')
        return render_template('auth_login.html', next_page=next_page)
    # 2. Post method, 处理登录请求
    username = request.form.get('username')
    password = request.form.get('password')
    # 2.1 login表单没有next参数时，next_page为None
    # 2.2 login表单有next参数时，next_page为对应字符串，如/admin/index
    next_page = request.form.get('next')
    # user = User.query.filter_by(username=username, password=password).first()
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return render_template('auth_login.html', warning="login failed!")
    # Default is remember=False
    login_user(user, remember=False)
    # login_user(user, remember=True)
    g.user = user
    return redirect(next_page or url_for('blue_main.vf_index'))
    # 当next_page不为空时，重定向至next_page
    # if next_page:
    #     return redirect(next_page)
    # 当next_page为空时，重定向至主页
    # else:
    #     return redirect(url_for('blue_main.vf_index'))


@blue_auth.route('/logout')
@viewfunclog
def logout():
    logout_user()
    return redirect(url_for('blue_auth.login'))
