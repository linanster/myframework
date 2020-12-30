SECRET_KEY = "youdonotknowme"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///../sqlite/db4_hist.sqlite3'
SQLALCHEMY_BINDS = {
'mysql_myframework_stu1': 'mysql+pymysql://root1:123456@localhost:3306/myframework',
'mysql_myframework_stu2': 'mysql+pymysql://root1:123456@localhost:3306/myframework',
'sqlite_db1_sys': 'sqlite:///../sqlite/db1_sys.sqlite3',
'sqlite_db2_app': 'sqlite:///../sqlite/db2_app.sqlite3',
'sqlite_db3_auth': 'sqlite:///../sqlite/db3_auth.sqlite3',
# 'sqlite_db4_hist': 'sqlite:///../sqlite/db4_hist.sqlite3',
}

# SECURITY_UNAUTHORIZED_VIEW = '/index'
