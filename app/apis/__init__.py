def init_apis(app):
    from app.apis.api_test import api_test
    from app.apis.api_auth import api_auth
    from app.apis.api_db_student import api_db_student
    from app.apis.api_file import api_file
    from app.apis.api_cmd import api_cmd
    api_test.init_app(app)
    api_auth.init_app(app)
    api_db_student.init_app(app)
    api_file.init_app(app)
    api_cmd.init_app(app)
