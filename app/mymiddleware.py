from flask import request

from app.lib.modelutils import add_visitcount

def load_middleware(app):
    
    @app.before_request
    def process_before():
        # 1. statistic/filter/prioritize
        # 2. authorization
        # print("==middleware==", request.url)
        add_visitcount()

    @app.after_request
    def process_after(response):
        return response
