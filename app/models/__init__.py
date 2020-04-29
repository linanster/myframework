from app.models.sqlite import db_sqlite
from app.models.sqlite import Sysinfo

def init_models(app):
    db_sqlite.init_app(app)
    db_sqlite.reflect(app=app)

