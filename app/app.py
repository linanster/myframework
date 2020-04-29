#coding:utf8
#
from flask import Flask
from app.models import init_models
from app.views import init_views
from app.apis import init_apis
from app.ext import init_ext

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('mysettings.py')
    init_models(app)
    init_views(app)
    init_apis(app)
    init_ext(app)
    return app
