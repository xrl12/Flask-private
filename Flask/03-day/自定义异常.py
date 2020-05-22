from flask import Flask, abort, Response,render_template

app = Flask(import_name=__name__,template_folder='../templates')


@app.route('/')
def index():
    abort(404)  # 直接传入一个状态吗
    # abort(Response('你好啊'))  # 返回一个resposne请求


# 自定义异常
@app.errorhandler(404)  # errorhandler里面的状态码必须是http状态吗
def my_error(error):
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
