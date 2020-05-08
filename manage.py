# coding:utf8
#
from flask_script import Manager
from app import create_app

app = create_app()

manager = Manager(app)

@manager.command
def hello():
    print('Hello, Manager Command!')

@manager.command
def createdb():
    from app.models.sqlite import db_sqlite, Sysinfo, Student
    db_sqlite.create_all(bind='sqlite1')
    db_sqlite.create_all(bind='sqlite2')
    Sysinfo.seed()
    Student.seed()

@manager.command
def deletedb():
    from app.models.sqlite import db_sqlite
    db_sqlite.drop_all(bind='sqlite1')
    db_sqlite.drop_all(bind='sqlite2')

@manager.option('--key', dest="key")
@manager.option('--field', dest="field")
# python3 manage.py get_sqlite --key r_running --field field1
def get_sqlite(key, field):
    from app.models.sqlite import Sysinfo
    print(Sysinfo.query.filter_by(key=key).first().get(field))

# python3 manage.py runserver -h 0.0.0.0 -p 5000 -r -d
if __name__ == '__main__':
    manager.run()
