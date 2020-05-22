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
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)


class ClassRoom(db.Model):
    __tablename__ = 'tab_class'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    create = db.Column(db.DateTime, default=datetime.now())
    students = db.relationship('Student', backref='classrooms')


class Score(db.Model):
    __tablename__ = 'tab_score'
    id = db.Column(db.Integer, primary_key=True)
    china = db.Column(db.Integer, nullable=False)
    math = db.Column(db.Integer, nullable=False)
    student = db.relationship('Student', backref='score', uselist=False)


class Student(db.Model):
    __tablename__ = 'tab_std'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    is_delete = db.Column(db.Boolean, default=False)
    cls_id = db.Column(db.Integer, db.ForeignKey('tab_class.id'))
    score_id = db.Column(db.Integer, db.ForeignKey('tab_score.id'))


@app.route('/')
def classroom():
    classrooms = ClassRoom.query.all()
    ctx = {
        "classrooms": classrooms
    }
    return render_template('homework/classroom.html', **ctx)


@app.route('/classroom/<int:id>/')
def student(id):
    classroom = ClassRoom.query.get(id)
    stus = classroom.students
    ctx = {
        'stus':stus
    }
    return render_template('homework/students.html',**ctx)


@app.route('/score/<int:id>')
def score(id):
    student = Student.query.get(id)
    scr = student.score
    ctx = {
        'scr':scr
    }
    return render_template('homework/score.html',**ctx)

if __name__ == '__main__':
    app.run(debug=True)
    # db.drop_all()
    # db.create_all()
    # room1 = ClassRoom(name='1901')
    # room2 = ClassRoom(name='1902')
    # room3 = ClassRoom(name='1903')
    #
    # db.session.add_all([room1, room2, room3])
    # db.session.commit()
    #
    # score1 = Score(china=80, math=80)
    # score2 = Score(china=100, math=100)
    # score3 = Score(china=30, math=89)
    # db.session.add_all([score1, score2, score3])
    # db.session.commit()
    #
    # studetn1 = Student(name='小徐一号', cls_id=room1.id, score_id=score1.id)
    # studetn2 = Student(name='小徐二号', cls_id=room2.id, score_id=score2.id)
    # studetn3 = Student(name='小徐三号', cls_id=room3.id, score_id=score3.id)
    # db.session.add_all([studetn1, studetn2, studetn3])
    # db.session.commit()
