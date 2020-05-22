from datetime import datetime

import pymysql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(import_name=__name__, template_folder='../templates')

pymysql.install_as_MySQLdb()
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/db_flask'

# 数据库和模型类同步修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始SQL语句
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_ECHO'] = False

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


@app.route('/index')
def index():
    cats = Cateogry.query.all()
    ctx = {
        'cats': cats
    }
    return render_template('04-查询数据.html', **ctx)


@app.route('/cat/<int:id>/')
def detail(id):
    news = New.query.filter_by(cat_id=id).all()  # 虽然只有一个，但是任然是返回列表
    ctx = {
        'news': news
    }
    print('----------------------------------------------{}------------------------'.format(news))
    return render_template('04-反向查询.html', **ctx)


@app.route('/test/<int:id>/')
def test(id):
    # cat = Cateogry.query.get(1)  # 默认是根据主键查询
    # news = Cateogry.query.filter(Cateogry.id == 1).all()
    # new = New.query.filter_by(id=1, title='新闻一').all()
    # new = New.query.filter(Cateogry.name.startswith('点')).all()
    # 跳过查询
    # new = New.query.offset(1).all()  # 跳过第一条数据
    # 分页
    # new1 = New.query.limit(1).all()  # 每次只查询一条
    # 倒叙
    # new1 = New.query.order_by(New.id.desc()).all()
    # 正序
    # new1 = New.query.order_by(New.id.asc()).all()
    # print(new1)
    # 分组
    # from sqlalchemy import func
    # # 第一个传入的是根据什么进行分组,第二个传入的是统计的个数
    # """
    # 返回的而数据：[(1, 1), (2, 1)]
    # 表示：分类id为1的有一个文章，分类id为2的id有一个文章
    # """
    # new = db.session.query(New.cat_id, func.count(New.cat_id)).group_by(New.cat_id).all()
    # print(new)

    # 逻辑或
    # from sqlalchemy import or_
    # new = New.query.filter(or_(New.id==1,New.title=='哈哈')).all() # 只需要匹配任意一个就OK

    #模糊查询
    # new = New.query.filter(New.title.contains('新闻')).all()

    # 获取个数
    new_count = New.query.count()
    print(new_count)

    return '其他的查询方法'


if __name__ == '__main__':
    app.run(debug=True)
