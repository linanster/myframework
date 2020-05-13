SECRET_KEY = "youdonotknowme"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/ge' 
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_BINDS = {
# 'mysql': 'mysql+pymysql://root:123456@localhost:3306/ge',
'sqlite_db1_sys': 'sqlite:///../sqlite/db1_sys.sqlite3',
'sqlite_db2_app': 'sqlite:///../sqlite/db2_app.sqlite3',
'sqlite_db3_auth': 'sqlite:///../sqlite/db3_auth.sqlite3',
'sqlite_db4_hist': 'sqlite:///../sqlite/db4_hist.sqlite3',
}


