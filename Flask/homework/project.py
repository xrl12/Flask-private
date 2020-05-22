import pymysql
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(import_name=__name__, template_folder='../templates')
pymysql.install_as_MySQLdb()
app.config['SECRET_KEY'] = 'asdfasdfasdfasdkfjdsal'
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/db_flask'

# 数据库和模型类同步修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'tab_user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    pwd = db.Column(db.String(32))


class Category(db.Model):
    __tablename__ = 'tab_cat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)


class Hero(db.Model):
    __tablename__ = 'tab_hero'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    cat_id = db.Column(db.INTEGER, db.ForeignKey('tab_cat.id'))


@app.route('/')
def index():
    uid = session.get('uid')
    user = User.query.get(uid)
    cats = Category.query.all()
    if user:
        ctx = {
            'user': user,
            'cats': cats
        }
        return render_template('homework/index.html', **ctx)
    ctx = {
        'cats': cats
    }
    return render_template('homework/index.html', **ctx)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('homework/register.html')
    elif request.method == 'POST':
        account = request.form.get('acc')
        pwd = request.form.get('pwd')
        if User.query.filter_by(name=account).first():
            ctx = {
                'error': "手机号已经注册"
            }
            return render_template('homework/register.html', **ctx)
        user = User(name=account,
                    pwd=pwd)
        db.session.add(user)
        db.session.commit()
        return '注册成功', '200 OK', {'Server': 'MyOwn'}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('homework/login.html')
    elif request.method == 'POST':
        acc = request.form.get('acc')
        pwd = request.form.get('pwd')
        user = User.query.filter_by(name=acc, pwd=pwd).first()
        if user:
            session['uid'] = user.id
            return redirect(url_for('index'))
        ctx = {
            'error': '账号或者密码不对'
        }
        return render_template('homework/login.html', **ctx)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/addc', methods=['POST'])
def add_category():
    name = request.form.get('cat')
    if Category.query.filter_by(name=name).first():
        return redirect(url_for('index'))
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/cat/<int:id>/',methods=['POST','GET'])
def show(id):
    if request.method == 'GET':
        heroes = Hero.query.filter(Hero.cat_id == id).all()
        ctx = {
            'heroes': heroes,
            'id': id
        }
        return render_template('homework/hero.html', **ctx)
    elif request.method == 'POST':
        hero_name = request.form.get('name')
        cid = request.form.get('cate')
        cat = Category.query.filter_by(id=cid).first()
        hero = Hero(name=hero_name,cat_id=cat.id)
        db.session.add(hero)
        db.session.commit()
        return redirect(request.url)


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True)
