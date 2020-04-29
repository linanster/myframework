from flask import Blueprint, request, render_template, flash, redirect, url_for
import os

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running


blue_test = Blueprint('blue_test', __name__, url_prefix='/test')

@blue_test.route('/')
@blue_test.route('/index')
@viewfunclog
def vf_index():
    status = get_running()
    return render_template('test_index.html', status=status)

