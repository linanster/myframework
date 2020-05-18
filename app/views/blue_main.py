from flask import Blueprint, request, render_template, flash, redirect, url_for
import os

from app.lib.mydecorator import viewfunclog
from app.lib.modelutils import get_running

from app.views.blue_test import blue_test


blue_main = Blueprint('blue_main', __name__)

@blue_main.route('/')
@blue_main.route('/index')
@viewfunclog
def vf_index():
    return render_template('main_index.html')
