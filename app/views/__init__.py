def init_views(app):
    from app.views.blue_test import blue_test
    from app.views.blue_main import blue_main
    from app.views.blue_auth import blue_auth
    from app.views.blue_admin import blue_admin
    app.register_blueprint(blue_test)
    app.register_blueprint(blue_main)
    app.register_blueprint(blue_auth)
    app.register_blueprint(blue_admin)
