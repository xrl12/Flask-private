from datetime import datetime

import pymysql
from flask import Flask
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


class Cateogry(db.Model):
    __tablename__ = 'flask_category'  # 指定一个表明
    id = db.Column(db.Integer, primary_key=True)  # 创建一个id，并且是主键
    name = db.Column(db.String(32), nullable=False)  # 创建分类名字,长度为32


class New(db.Model):
    __tablename__ = 'flask_news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=True)
    nvum = db.Column(db.Integer, default=0)
    content = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    cat_id = db.Column(db.Integer, db.ForeignKey('flask_category.id'))  # ! 注意，这里的外建不是类名,而是表民.字段


if __name__ == '__main__':
    # db.drop_all()  # 删除全部
    # db.create_all()  # 重新创建表

    """
    添加单个数据
    """
    # cat1 = Cateogry(name='热点')
    # db.session.add(cat1)
    # db.session.commit()

    """
    添加多个数据
    """
    # cat1 = Cateogry(name='热点')
    # cat2 = Cateogry(name='科技')
    # db.session.add_all([cat1, cat2])
    # db.session.commit()
    #
    # new1 = New(title='新闻一', content='新闻一', cat_id=cat1.id)
    # new2 = New(title='新闻二', content='新闻二', cat_id=cat2.id)
    # db.session.add_all([new1, new2])
    # db.session.commit()
    app.run(debug=True)
