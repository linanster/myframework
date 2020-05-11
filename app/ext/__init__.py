def init_ext(app):
    from app.ext.bootstrap import bootstrap
    from app.ext.loginmanager import login_manager
    bootstrap.init_app(app)
    login_manager.init_app(app)
