from flask import Flask, flash, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired

app = Flask(import_name=__name__, template_folder='../templates')

app.config['SECRET_KEY'] = 'dafldsjflkasdfjlasdfa;l'


class LoginForm(FlaskForm):
    name = StringField(label='用户名',
                       validators=[DataRequired('这个是必填的'), Length(min=3, max=10, message='最小的长度是3，最大的长度是10')])
    pwd = PasswordField(label='密码', validators=([DataRequired('密码是必填的')]))
    submit = SubmitField(label='提交')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     login = LoginForm()
#     if request.method == 'GET':
#         return render_template('flash/flash.html', login=login)
#     elif request.method == 'POST':
#         if login.validate_on_submit():
#             flash('登录成功')
#         return redirect(request.url)

@app.route('/', methods=['GET', 'POST'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('flash/flash.html', login=login)
    elif request.method == 'POST':
        if login.validate_on_submit():
            flash('登录成功',category='success')
        flash('登录失败',category='error')
        flash('我在测试',category='play')
        return redirect(request.url)


if __name__ == '__main__':
    app.run(debug=True)
