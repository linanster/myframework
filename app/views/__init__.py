def init_views(app):
    from app.views.blue_test import blue_test
    app.register_blueprint(blue_test)
