from flask import Flask, render_template, request
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo, ValidationError

app = Flask(import_name=__name__, template_folder='../templates')

app.config['SECRET_KEY'] = 'nihaoa '


# 使用form表单进行验证
class LoginForm(FlaskForm):
    phone = StringField(label='手机号', validators=[DataRequired('手机号不能为空')])
    pwd = PasswordField(label='密码', validators=[DataRequired('密码是必填的')])
    pwd2 = PasswordField(label='再次输入密码', validators=[DataRequired('密码是必填的'), EqualTo('pwd', '两次密码输入不一样')])
    submit = SubmitField(label='提交')

    def validate_phone(self, field):
        if field.data == '徐瑞鑫是个灵才才':
            raise ValidationError('你说错了')


@app.route('/', methods=['POST', 'GET'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('form/login.html', login=login)
    elif request.method == 'POST':
        if login.validate_on_submit():
            phone = login.phone.data
            pwd = login.pwd.data
            pwd2 = login.pwd2.data
            print(phone, pwd, pwd2)
            return 'OK'
        return render_template('form/login.html', login=login)


if __name__ == '__main__':
    app.run(debug=True)
