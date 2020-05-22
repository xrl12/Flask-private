from flask import Flask, current_app

app = Flask(__name__)

app.config.from_pyfile('config.cfg')


# app.debug = True


@app.route('/index')
def index():
    # im   g_format = app.config.get('IMG_FORMAT')  # 获取配置文件的内容
    # print(img_format)

    img_format = current_app.config.get("IMG_FORMAT")  # 使用全局的方法获取配置文件里面的内容
    print(img_format)

    return '这里是主页'


if __name__ == '__main__':
    app.run()
