from flask import Flask,make_response,render_template,request
from datetime import datetime
app = Flask(import_name=__name__,template_folder='../templates')


@app.route('/')
def index():
    uid = request.cookies.get('uid')
    print(uid)
    return make_response(render_template('set_cookie.html'))


# 保存cookie
@app.route('/login')
def login():
    response = make_response(render_template('set_cookie.html'))
    # response.set_cookie('uid','123',max_age = 5)  # 表示cookie的过期时间是五秒
    response.set_cookie('uid','123',expires=datetime(year=2020,month=5,day=12,hour=18,minute=55))  # 表示cookie的过期时间是2020年5月12日18点55分过期
    return response


# 删除cookie
@app.route('/delete')
def del_cookie():
    response = make_response('删除cookie')
    response.delete_cookie('uid')
    return response


if __name__ == '__main__':
    app.run(debug=True)