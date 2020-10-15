from flask import Blueprint, request, render_template, flash, redirect, url_for
from app.lib.mydecorator import viewfunclog


blue_error = Blueprint('blue_error', __name__, url_prefix='/error')


@blue_error.route('/')
@blue_error.route('/index')
@viewfunclog
def vf_index():
    return render_template('error_index.html')
