from flask import Flask

app = Flask(import_name=__name__)
app.config['DEBUG'] = True


# @app.route('/index/<int:id>')  # 不支持负数
# def index1(id):
#     print(id)
#     return '你好啊，臭弟弟'


# @app.route("/index/<int(signed=True):id>")  # 可以匹配到负数
# def index2(id):
#     print(id)
#     return '你好啊'


# @app.route('/<default:user_name>')
# def idnex3(user_name):
#     print(user_name)
#     return '你好啊'
#
#
# @app.route('/<string:username>')
# def index4(username):
#     print(username)
#     return '你好啊'


@app.route('/<string(length=2):username>')
def index4(username):
    print(username)
    return '你好啊'


# @app.route('/index/<uuid:id>')
# def index5(id):
#     print(id)
#     return str(id)
#
#
# @app.route('/index/<path:user>')
# def index6(user):
#     print(user)
#     return '我是path'


# @app.route('/index/<float:num>')
# # def index7(num):
# #     print(num)
#     return '我是num'


# -------------------------------------------------------------------------------->
# 自定义转换器
# class PhoneConverter(BaseConverter):
#
#     def __init__(self,map):
#         super().__init__(map)
#         self.regex = r'123$'
#
#     def to_python(self, value):
#         return value  # 控制传来的参数
#
#     def to_url(self, value):
#         return value  # 控制反向解析
#
# app.url_map.converters['phone'] = PhoneConverter
#
#
# @app.route('/index/<phone:user_phone>')
# def index8(user_phone):
#     print(user_phone)
#     return '你好啊'


# ------------------------------------------------------------------------------->
# # 高级转化器
# class MyConverter(BaseConverter):
#     def __init__(self,map,regex):
#         super().__init__(map)
#         self.regex = regex


# app.url_map.converters['high'] = MyConverter
# @app.route('/index1/<high(".*?"):id>')
# def index(id):
#     return '这是我使用高级高级转化器'


if __name__ == '__main__':
    app.run()
