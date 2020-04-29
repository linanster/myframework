def init_ext(app):
    from app.ext.bootstrap import bootstrap
    bootstrap.init_app(app)
