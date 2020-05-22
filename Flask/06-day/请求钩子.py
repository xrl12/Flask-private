from flask import Flask,request

app = Flask(import_name=__name__)


@app.before_first_request
def before_first_request():
    print('我就执行一次')


@app.before_request
def before_request():
    print(request.remote_addr)

    print('我在每一次请求都会执行的哦')


@app.after_request
def after_request(response):
    print('我执行这个方法了')
    return response


@app.teardown_request
def teardown_request(error):
    print('error = {}'.format(error))


@app.route('/')
def index():
    return '123'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
