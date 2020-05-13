# coding:utf8
#
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import copy

from app import create_app
from app.models import db_sqlite

app = create_app()

migrate = Migrate(app, db_sqlite)

manager = Manager(app)

# python3 manage.py db init --multidb
# python3 manage.py db migrate [--message MESSAGE]
# python3 manage.py db upgrade [--tag TAG]
# python3 manage.py db downgrade [--tag TAG]
# python3 manage.py db history
manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    "my cmd: just say hello"
    print('Hello, Manager Command!')

@manager.command
# python3 manage.py createdb
# python3 manage.py createdb --init
def createdb(init=False):
    "my cmd: create all database and initialize data"
    from app.models.sqlite import db_sqlite, Sysinfo, Student, User
    if init:
        Sysinfo.seed()
        Student.seed()
        User.seed()
    else:
        db_sqlite.create_all(bind='sqlite_db1')
        db_sqlite.create_all(bind='sqlite_db2')
        db_sqlite.create_all(bind='sqlite_auth')

@manager.command
# python3 manage.py deletedb --uninit
# python3 manage.py deletedb
def deletedb(uninit=False):
    "my cmd: delete all database tables and datas"
    from app.models.sqlite import db_sqlite, Sysinfo, Student, User
    if uninit:
        Sysinfo.query.delete()
        Student.query.delete()
        User.query.delete()
        db_sqlite.session.commit()
    else:
        db_sqlite.drop_all(bind='sqlite_db1')
        db_sqlite.drop_all(bind='sqlite_db2')
        db_sqlite.drop_all(bind='sqlite_auth')

@manager.option('-k', '--key', dest="key", default='r_running')
@manager.option('-f', '--field', dest="field", default='field1')
# python3 manage.py get_sysinfo
# python3 manage.py get_sysinfo -k r_running -f field1
# python3 manage.py get_sysinfo --key r_running --field field1
def get_sysinfo(key, field):
    "my cmd: get data from db sysinfos"
    from app.models.sqlite import Sysinfo
    print(Sysinfo.query.filter_by(key=key).first().get(field))

@manager.command
# python3 manage.py
# python3 manage.py get_student -n='nan'
# python3 manage.py get_student --name='nan'
def get_student(name='nan'):
    "my cmd: get data from db students"
    from app.models.sqlite import Student
    stu = Student.query.filter_by(name=name).first()
    if stu:
        stu = copy.deepcopy(stu.__dict__)
        stu.pop('_sa_instance_state')
        stu.pop('id')
        print(stu)



# python3 manage.py runserver -h 0.0.0.0 -p 5000 -r -d
if __name__ == '__main__':
    manager.run()
