SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/ge' 
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_BINDS = {
# 'mysql': 'mysql+pymysql://root:123456@localhost:3306/ge',
'sqlite_db1': 'sqlite:///../sqlite/db1.sqlite3',
'sqlite_db2': 'sqlite:///../sqlite/db2.sqlite3',
'sqlite_auth': 'sqlite:///../sqlite/auth.sqlite3',
}


