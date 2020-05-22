import pymysql

from flask import Flask, request, render_template
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


class New(db.Model):
    __tablename__ = 'tab_news'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


@app.route('/<int:id>', methods=['GET','POST'])
def index(id):
    if request.method == 'GET':
        news = New.query.all()
        ctx = {
            'news': news
        }
        return render_template('跟新数据/更新数据.html', **ctx)
    new = New.query.get(id)
    new.name = request.form.get('name')
    db.session.add(new)
    db.session.commit()
    return 'OK'


@app.route('/del/<int:id>')
def deldata(id):
    new = New.query.get(id)
    db.session.delete(new)
    db.session.commit()
    return '删除成功'




if __name__ == '__main__':
    # db.create_all()
    # new = New(name='新闻一')
    # db.session.add(new)
    # db.session.commit()
    app.run(debug=True)
