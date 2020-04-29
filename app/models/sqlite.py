from flask_sqlalchemy import SQLAlchemy
import datetime

db_sqlite = SQLAlchemy(use_native_unicode='utf8')


class Sysinfo(db_sqlite.Model):
    __bind_key__ = 'sqlite'
    __tablename__ = 'sysinfo'
    id = db_sqlite.Column(db_sqlite.Integer, nullable=False, autoincrement=True, primary_key=True)
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

