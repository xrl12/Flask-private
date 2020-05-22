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
app.config['SQLALCHEMY_ECHO'] = False

db = SQLAlchemy(app)

"""
一对一
当表的关系为一对一时：如果需要添加反向解析，则需要把uselist=False
"""

"""
一对一
"""


class Student(db.Model):
    __tablename__ = 'tab_stu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    scr = db.Column(db.Integer, db.ForeignKey('tab_scr.id'))


class Score(db.Model):
    __tablename__ = 'tab_scr'
    id = db.Column(db.Integer, primary_key=True)
    china_score = db.Column(db.Integer, nullable=False)
    stu = db.relationship(Student, backref='score', uselist=False)


# 一对多 和 多对多
# 使用多对多的时候我们需要自己在建立一个表,来表现出他们的关系
tags = db.Table(
    'tab_tag_art',
    db.Column('id', db.Integer, primary_key=True),  # 主键
    db.Column('tag_id', db.Integer, db.ForeignKey('tab_tag.id')),  # 标签id
    db.Column('art_id', db.Integer, db.ForeignKey('tab_art.id'))  # 文章id
)


class Article(db.Model):
    __tablename__ = 'tab_art'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('tab_cat.id'))
    tags = db.relationship('Tag', backref='arts', secondary=tags)


class Category(db.Model):
    __tablename__ = 'tab_cat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    arts = db.relationship(Article, backref='arts')  # 一对多反向解析


class Tag(db.Model):
    __tablename__ = 'tab_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


# 自关联
class Area(db.Model):
    __tablename__ = 'tab_area'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    parent_id = db.Column(db.Integer, db.ForeignKey('tab_area.id'))
    parent = db.relationship('Area', remote_side=[id])

    def __str__(self):
        return self.name


# 查询一对一
@app.route('/')
def index():
    # 当学生查询成绩的时候
    # student = Student.query.get(1)
    # print(student.score)  # 返回的是一个对象，

    # 当通过成绩查询学生的时候
    score = Score.query.get(1)
    print(score.stu)
    return '你好啊'


# 查询一对多
@app.route('/index1')
def index1():
    cat = Category.query.get(1)
    print('这里是cat = {}'.format(cat))
    arts = cat.arts
    for art in arts:
        print('这个是{}分类下的文章{}'.format(cat, art))
        print('这个是{}文章的标签{}'.format(art, art.tags))
        print('---------------------------------------------------------')
        return '年后啊'


# 查询自关联
@app.route('/index2/<int:id>')
def index2(id):
    area = Area.query.filter(Area.id==id).first()
    print(area.parent)
    print(area.query.filter(Area.parent_id==area.id).first())
    return 'nihao '


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #
    # """
    #     一对一：
    #         添加数据：
    # """
    # score1 = Score(china_score=100)
    # score2 = Score(china_score=80)
    # score3 = Score(china_score=60)
    # db.session.add_all([score3, score2, score1])
    # db.session.commit()
    #
    # student1 = Student(name='小红', scr=score1.id)
    # student2 = Student(name='小明', scr=score2.id)
    # student3 = Student(name='小蓝', scr=score3.id)
    # db.session.add_all([student1, student2, student3])
    # db.session.commit()

    # -------------------------------------------------------------------
    # 一对多添加数据
    # category1 = Category(name='热点')
    # category2 = Category(name='科技')
    # category3 = Category(name='医学')
    # db.session.add_all([category1, category2, category3])
    # db.session.commit()
    #
    # article1 = Article(title='热点新闻', cat_id=category1.id)
    # article2 = Article(title='科技新闻', cat_id=category2.id)
    # article3 = Article(title='医学新闻', cat_id=category3.id)
    # db.session.add_all([article1, article2, article3])
    # db.session.commit()
    #
    # # -------------------------------------------------------------------
    # # 多对多添加数据
    # tag1 = Tag(name='标签1')
    # tag2 = Tag(name='标签2')
    # tag3 = Tag(name='标签3')
    # db.session.add_all([tag1, tag2, tag3])
    # db.session.commit()
    #
    # article1.tags = [tag1, tag2]
    # article2.tags = [tag3, tag2]
    # article3.tags = [tag1, tag3]
    # db.session.commit()


# ------------------------------------------------------------------------------------------------------->

    # area1 = Area(name='山西')
    # area2 = Area(name='北京')
    # db.session.add_all([area1, area2])
    # db.session.commit()
    #
    # area3 = Area(name='忻州', parent_id=area1.id)
    # db.session.add(area3)
    # db.session.commit()
    app.run(debug=True)
