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


class Category(db.Model):
    __tablename__ = 'tab_cat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


# 多对多中间表
tag = db.Table(
    'tab_midden_tag',  # 表名
    db.Column('tag_id', db.Integer, db.ForeignKey("tab_tag.id")),
    db.Column('art_id', db.Integer, db.ForeignKey("tab_art.id")),
)


class Article(db.Model):
    __tablename__ = 'tab_art'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    cat_id = db.Column(db.Integer, db.ForeignKey("tab_cat.id"))
    tags = db.relationship('Tag', backref='articles', secondary=tag)


class Tag(db.Model):
    __tablename__ = 'tab_tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


@app.route('/')
def index():
    art = Article.query.filter(Article.id == 1).first()
    tags = art.tags
    for tag in tags:
        print(tag.articles)
    print(art)
    return '你好啊'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    cat1 = Category(name='分类一')
    cat2 = Category(name='分类二')
    db.session.add_all([cat1, cat2])
    db.session.commit()

    tag1 = Tag(name='标签一')
    tag2 = Tag(name='标签二')
    tag3 = Tag(name='标签三')
    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()

    art1 = Article(title='文章一', cat_id=cat1.id)
    art2 = Article(title='文章2', cat_id=cat2.id)
    db.session.add_all([art1, art2])
    # art1.tags = [tag1,tag2]
    # art2.tags = [tag2,tag3]
    db.session.commit()

    # app.run(debug=True)
