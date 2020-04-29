def init_apis(app):
    from app.apis.api_test import apitest
    apitest.init_app(app)
