from flask import Flask

# 没有使用static_url_path 时候的路由：http://127.0.0.1:5000/static/images/2.jpeg
# 使用static_url_path 时候的路由：http://127.0.0.1:5000/abc/images/2.jpeg
app = Flask(import_name=__name__, static_folder='../static',static_url_path='/abc')


@app.route('/')
def index():
    return '你好啊'

if __name__ == '__main__':
    app.run(debug=True)