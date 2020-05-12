from flask import Blueprint, request, render_template, flash, redirect, url_for
import os

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running


blue_admin = Blueprint('blue_admin', __name__, url_prefix='/admin')

@blue_admin.route('/')
@blue_admin.route('/index')
@viewfunclog
def vf_index():
    return render_template('admin_index.html')

@blue_admin.route('/config')
@viewfunclog
def vf_config():
    return render_template('admin_config.html')
