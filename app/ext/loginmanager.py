from flask_login import LoginManager
from app.models.sqlite import User
from app.views.blue_auth import blue_auth

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'blue_auth.login'

def init_loginmanager(app):
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
