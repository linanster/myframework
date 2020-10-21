# coding:utf8
#
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import copy

from app import create_app, envinfo
from app.models import db_sqlite

import sys

app = create_app()

migrate = Migrate(app, db_sqlite)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def hello():
    "my cmd: just say hello"
    print('Hello, Manager Command!')

@manager.command
# python3 manage.py createdb_sqlite [--table] [--data] [--hist]
def createdb_sqlite(table=False, data=False, hist=False):
    "my cmd: create all database and initialize datas"
    from app.models.sqlite import db_sqlite, Sysinfo, Student, User, Pin, StatsCount
    print('==create databases==')
    if table:
        print('==create tables==')
        db_sqlite.create_all(bind='sqlite_db1_sys')
        db_sqlite.create_all(bind='sqlite_db2_app')
        db_sqlite.create_all(bind='sqlite_db3_auth')
    if data:
        print('==initialize datas==')
        Sysinfo.seed()
        Student.seed()
        User.seed()
        Pin.seed()
    if hist:
        print('legacy command, exit!')
        return 0
        print('==create history tables==')
        db_sqlite.create_all(bind='sqlite_db4_hist')
        StatsCount.seed()

@manager.command
# python3 manage.py deletedb_sqlite [--table] [--data] [--hist]
def deletedb_sqlite(table=False, data=False, hist=False):
    "my cmd: delete all database tables and datas"
    from app.models.sqlite import db_sqlite, Sysinfo, Student, User, Pin, StatsCount
    if table:
        print('==delete tables==')
        db_sqlite.drop_all(bind='sqlite_db1_sys')
        db_sqlite.drop_all(bind='sqlite_db2_app')
        db_sqlite.drop_all(bind='sqlite_db3_auth')
        return
    if data:
        print('==delete datas==')
        Sysinfo.query.delete()
        Student.query.delete()
        User.query.delete()
        Pin.query.delete()
        db_sqlite.session.commit()
    if hist:
        print('legacy command, exit!')
        return 0
        print('==delete history tables==')
        db_sqlite.drop_all(bind='sqlite_db4_hist')

@manager.command
def init_hist():
    "my cmd: run StatsCount.seed()"
    from app.models.sqlite import db_sqlite, StatsCount
    print('==insert initial history data==')
    StatsCount.seed()

@manager.command
def cleanup(log=False, pycache=False, all=False):
    "my cmd: clean up logs and __pycache__"
    from app.lib.myutils import cleanup_log, cleanup_pycache
    if all or log:
        print('==cleanup log==')
        cleanup_log()
    if all or pycache:
        print('==cleanup pycache==')
        cleanup_pycache()


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


@app.template_global('now')
def get_now_timestamp():
    import time
    return time.time()

@app.template_global('visitcount')
def get_visitcount():
    from app.lib.modelutils import get_visitcount
    return get_visitcount()

@app.template_filter('timeformat')
def timeformat(timestamp):
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))




# python3 manage.py runserver -h 0.0.0.0 -p 5000 -r -d
if __name__ == '__main__':
    # envinfo()
    manager.run()
