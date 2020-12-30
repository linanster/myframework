from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
from dateutil import tz



# 1. lasy init
db_mysql = SQLAlchemy(use_native_unicode='utf8')


# 2. model definition

class MyBaseModel(db_mysql.Model):

    __abstract__ = True

    id = db_mysql.Column(db_mysql.Integer, nullable=False, autoincrement=True, primary_key=True)

    def save(self):
        try:
            db_mysql.session.add(self)
            db_mysql.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db_mysql.session.delete(self)
            db_mysql.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

class Stu1(MyBaseModel):
    __bind_key__ = 'mysql_myframework_stu1'
    __tablename__ = 'stu1'
    name = db_mysql.Column(db_mysql.String(100), nullable=False, unique=True)
    age = db_mysql.Column(db_mysql.Integer)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def seed():
        stu1 = Stu1('allen', 31)
        stu2 = Stu1('nan', 32)
        stu3 = Stu1('jun', 33)
        db_mysql.session.add_all([stu1, stu2, stu3])
        db_mysql.session.commit()

class Stu2(MyBaseModel):
    __bind_key__ = 'mysql_myframework_stu2'
    __tablename__ = 'stu2'
    name = db_mysql.Column(db_mysql.String(100), nullable=False, unique=True)
    age = db_mysql.Column(db_mysql.Integer)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def seed():
        stu1 = Stu2('allen', 31)
        stu2 = Stu2('nan', 32)
        stu3 = Stu2('jun', 33)
        db_mysql.session.add_all([stu1, stu2, stu3])
        db_mysql.session.commit()

