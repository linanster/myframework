from flask import Blueprint, request, render_template, flash, redirect, url_for
import os
from flask_login import login_required

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running

from app.views.blue_test import blue_test


blue_index = Blueprint('blue_index', __name__)

@blue_index.route('/')
@blue_index.route('/index')
@login_required
@viewfunclog
def vf_index():
    return redirect(url_for('blue_test.vf_index'))
