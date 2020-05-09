from flask_sqlalchemy import SQLAlchemy
import datetime

db_sqlite = SQLAlchemy(use_native_unicode='utf8')


class MyBaseModel(db_sqlite.Model):

    __abstract__ = True

    id = db_sqlite.Column(db_sqlite.Integer, nullable=False, autoincrement=True, primary_key=True)

    def save(self):
        try:
            db_sqlite.session.add(self)
            db_sqlite.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db_sqlite.session.delete(self)
            db_sqlite.session.commit()
            return True
        except Exception as e:
            print(e)
            return False            


# class Sysinfo(db_sqlite.Model):
class Sysinfo(MyBaseModel):
    __bind_key__ = 'sqlite1'
    __tablename__ = 'sysinfos'
    # id = db_sqlite.Column(db_sqlite.Integer, nullable=False, autoincrement=True, primary_key=True)
    key = db_sqlite.Column(db_sqlite.String(100))
    field1 = db_sqlite.Column(db_sqlite.Boolean)
    field2 = db_sqlite.Column(db_sqlite.Integer)
    field3 = db_sqlite.Column(db_sqlite.String(100))
    description = db_sqlite.Column(db_sqlite.String(100))
    def __init__(self, key, field1=False, field2=0, field3='', description=''):
        self.key = key
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3
        self.description = description
    def get(self, field):
        return {'field1':self.field1, 'field2':self.field2, 'field3':self.field3}.get(field)
    @staticmethod
    def seed():
        r_running = Sysinfo('r_running', field1=False, description='Indicate running or not, default is False.')
        seeds = [r_running,] 
        db_sqlite.session.add_all(seeds)
        db_sqlite.session.commit()


# class Student(db_sqlite.Model):
class Student(MyBaseModel):
    __bind_key__ = 'sqlite2'
    __tablename__ = 'students'
    # id = db_sqlite.Column(db_sqlite.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = db_sqlite.Column(db_sqlite.String(100))
    age = db_sqlite.Column(db_sqlite.Integer)
    exampass = db_sqlite.Column(db_sqlite.Boolean)
    # enrolltime = db_sqlite.Column(db_sqlite.DateTime)
    # enrolltime = db_sqlite.Column(db_sqlite.DateTime, default=datetime.datetime.datetime.now())
    enrolltime = db_sqlite.Column(db_sqlite.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    def __init__(self, name, age, exampass):
        self.name = name
        self.age = age
        self.exampass = exampass
        # self.enrolldate = enrolldate
    @staticmethod
    def seed():
        # date_obj_1 = datetime.datetime(2020, 5, 8, 19, 40, 0)
        # date_str_1 = date_obj_1.strftime('%Y-%m-%d %H:%M:%S')
        # date_str_2 = '2020-05-08 19:40:00'
        # s1 = Student('allen', 29, False, date_obj_1)
        # s2 = Student('nan', 32, True, date_str_1)
        # s3 = Student('jun', 33, False, date_str_2)
        s1 = Student('allen', 29, False)
        s2 = Student('nan', 32, True)
        s3 = Student('jun', 33, False)
        seeds = [s1, s2, s3] 
        db_sqlite.session.add_all(seeds)
        db_sqlite.session.commit()

