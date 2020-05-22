from flask import Flask

app = Flask(import_name=__name__)


# 通过引用文件的方法导入配置文件
# app.config.from_pyfile('config.cfg')


# 使用类方法导入配置文件
# class Config(object):
#     Debug = True
#
# app.config.from_object(Config)

# 直接使用应用进行配置
# app.debug = True

# 直接导入配置文件
# app.config['DEBUG'] = True

# 使用对象来配置文件
# app.debug = True


@app.route('/index')
def index():
    return '你好啊啊'


if __name__ == '__main__':
    # 再启动的时候进行配置
    app.run(host='0.0.0.0', port=8000, debug=True)  # 本机的任意一个ip都可以访问
