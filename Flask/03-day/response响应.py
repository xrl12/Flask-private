from flask import Flask, make_response,jsonify
import json

app = Flask(import_name=__name__)


@app.route('/')
def index():
    # 在添加请求头的时候不要添加中文
    # return '你好啊', '10000 OK', {"Server": 'Hello'}    # 这里应该返回一个元祖,可以加括号,也可以不加括号
    # return ('你好啊', '10000 OK', {"Server": 'Hello'})    # 这里应该返回一个元祖,可以加括号,也可以不加括号
    response = make_response('自定义响应')
    response.headers['name'] = 'xuruixin'
    response.headers['Server'] = 'adfasdaf'
    return response


@app.route('/get_json')
def get_json():
    ctx = {
        'name': "xuruixin",
        "gender": "男",
        "age": "11"
    }
    # 手动把字符串变成json数据
    # data = json.dumps(ctx)
    # response = make_response(data)
    # response.headers['content-type'] = 'application/json'

    # Flask 自动把字符串变成json数据
    response = jsonify(ctx)
    return response




if __name__ == '__main__':
    app.run(debug=True)
