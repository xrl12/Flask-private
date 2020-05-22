import pymysql
from flask import Flask
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


class ClassRoom(db.Model):
    __tablename__ = 'tab_room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=True, unique=True)
    students = db.relationship('Student', backref='classroom')


class Student(db.Model):
    __tablename__ = 'tab_stu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    class_id = db.Column(db.Integer, db.ForeignKey('tab_room.id'))


@app.route('/')
def index():
    # 通过反向查找
    # student = Student.query.filter(Student.id==1).first()
    # print(student.classroom)

    classroom = ClassRoom.query.filter(ClassRoom.id==1).first()
    print(classroom.students)

    # # 通过class_id进行查找
    # classroom = Student.query.filter(Student.class_id == 1).all()
    # print(classroom)

    return 'asdfa'


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # room1 = ClassRoom(name=1903)
    # room2 = ClassRoom(name=1907)
    # room3 = ClassRoom(name=1910)
    # db.session.add_all([room1,room2,room3])
    # db.session.commit()
    #
    # stu1 = Student(name='小徐一号',class_id=room1.id)
    # stu2 = Student(name='小徐二号',class_id=room2.id)
    # stu３ = Student(name='小徐三号',class_id=room3.id)
    # stu4 = Student(name='小徐四号',class_id=room1.id)
    # db.session.add_all([stu1,stu2,stu３,stu4])
    # db.session.commit()
    app.run(debug=True)
