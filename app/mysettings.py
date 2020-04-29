SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
SQLALCHEMY_TRACK_MODIFICATIONS = False
HOST = '0.0.0.0'
PORT = 4000
DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/ge' 
SQLALCHEMY_BINDS = {
# 'mysql': 'mysql+pymysql://root:123456@localhost:3306/ge',
'sqlite': 'sqlite:///../sqlite/db.sqlite3'
}


