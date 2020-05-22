import pymysql
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()
app = Flask(__name__)
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/db_flask'

# 数据库和模型类同步修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

manage = Manager(app)

Migrate(app=app, db=db)  # 创建一个数据库迁移对象

manage.add_command('db', MigrateCommand)


class New(db.Model):
    __tablename__ = 'tab_news'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


class Category(db.Model):
    __tablename__ = 'ab_cat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    content = db.Column(db.String(21))
    new = db.Column(db.String(32))


if __name__ == '__main__':
    manage.run()
