def init_apis(app):
    from app.apis.api_test import api_test
    from app.apis.api_auth import api_auth
    from app.apis.api_db_student import api_db_student
    api_test.init_app(app)
    api_auth.init_app(app)
    api_db_student.init_app(app)
