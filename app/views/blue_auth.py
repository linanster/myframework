from flask import Blueprint, request, render_template, flash, redirect, url_for
import os
from flask_login import login_user, logout_user, login_required

from app.models.sqlite import User
from app.lib.mydecorator import viewfunclog
from app.lib.mylogger import logger_module1
from app.views.blue_index import blue_index


blue_auth = Blueprint('blue_auth', __name__, url_prefix='/auth')

@blue_auth.route('/login', methods=['GET', 'POST'])
@viewfunclog
def login():
    logger_module1.warn('client from {}'.format(request.remote_addr))
    if request.method == 'GET':
        return render_template('auth_login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    # user = User.query.filter_by(username=username, password=password).first()
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return render_template('auth_login.html', warning="login failed!")
    else:
        login_user(user)
        return redirect(url_for('blue_index.vf_index'))

@blue_auth.route('/logout')
@viewfunclog
def logout():
    logout_user()
    return redirect(url_for('blue_auth.login'))
