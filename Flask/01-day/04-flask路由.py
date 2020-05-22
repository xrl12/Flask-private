from flask import Flask, redirect, url_for

app = Flask(import_name=__name__)
app.config.from_pyfile('config.cfg')


@app.route('/')
def index():
    return '你好啊'


@app.route('/content')
def index2():
    # return 'niho'
    return redirect(url_for('index'))  # 里面传入的是字符串不是函数的引用


@app.route('/method', methods=['POST'])
def index3():
    return '你好啊'


if __name__ == '__main__':
    app.run()
