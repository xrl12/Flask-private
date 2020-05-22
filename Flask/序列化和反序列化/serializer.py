import pymysql
from flask import Flask,jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(import_name=__name__)
ma = Marshmallow(app)

pymysql.install_as_MySQLdb()
# 设置连接数据库的URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/db_flask'

# 数据库和模型类同步修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_ECHO'] = False

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
db = SQLAlchemy(app=app)


class Student(db.Model):
    __tablename__ = 'tab_stu'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(32))
    cls_id = db.Column(db.Integer, db.ForeignKey('tab_cls.id'))


class ClassRoom(db.Model):
    __tablename__ = 'tab_cls'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)


class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "phone", "name", "cls_id")

    # Smart hyperlinkin
    _links = ma.Hyperlinks(
        {"self": ma.URLFor("user_detail", id="<id>"), "collection": ma.URLFor("users")}
    )


user_schema = StudentSchema()
users_schema = StudentSchema(many=True)


@app.route("/api/users/")
def users():
    all_users = Student.query.all()
    print(all_users)
    print(users_schema.dump(all_users))
    return jsonify(users_schema.dump(all_users))
    # return users_schema.dump(all_users)


@app.route("/api/users/<id>")
def user_detail(id):
    user = Student.query.get_or_404(id)
    return user_schema.dump(user)


if __name__ == '__main__':
    app.run(debug=True)
    # db.drop_all()
    # db.create_all()
    #
    # cls1 = ClassRoom(name='1907')
    # cls2 = ClassRoom(name='1910')
    # cls3 = ClassRoom(name='1903')
    # db.session.add_all([cls1, cls2, cls3])
    # db.session.commit()
    #
    # student1 = Student(name='小徐一号', phone='13096575411', cls_id=cls1.id)
    # student2 = Student(name='小徐二号', phone='13096575412', cls_id=cls2.id)
    # student3 = Student(name='小徐三号', phone='13096575413', cls_id=cls3.id)
    #
    # db.session.add_all([student1, student2, student3])
    # db.session.commit()
