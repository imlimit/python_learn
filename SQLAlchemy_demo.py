#-*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aa:aa@localhost/blog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:\code\python\data1yy.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)  #DB为SQLAlchemy实例
print("OK")

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Rolr(db.Model):
    __tablename__ = 'Rolr'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

db.drop_all()  #删除旧表
db.create_all()  #创建新表

user_john = User(username='john',email='123@123.com')
user_tom = User(username='tom',email='1234@123.com')
user_ti = User(username='ti',email='1235@123.com')

db.session.add(user_john)
db.session.add(user_tom)
db.session.add(user_ti)   #数据库会话

db.session.commit()      #改动写入数据库

print user_john.id
print user_tom.id
print user_ti.id

user_john.username = 'hoho'
db.session.add(user_john)
db.session.commit()       #数据库修改
print user_john.username

db.session.delete(user_john)
db.session.commit()         #删除行

print User.query.all()  #查询数据库中所有记录
print str(User.query.filter_by(username='ti'))    #等值过滤器查询数据库中所有记录


