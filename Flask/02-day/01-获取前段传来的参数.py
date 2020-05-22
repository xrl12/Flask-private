from flask import Flask, render_template, request

app = Flask(import_name=__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    print("request.form={}".format(request.form))
    print("request.data={}".format(request.data))  # 请求方法为POST的时候获取参数
    print("request.url={}".format(request.url))
    print("request.args={}".format(request.args))  # 请求方法为GET的时候可以获取参数
    # print(request.data.decode('utf8').get('pwd'))
    # print(request.data.decode('utf8').getlist('happy'))
    print(request.form.get('pwd'))
    print(request.form.getlist('happy'))
    return 'nihoa'


if __name__ == '__main__':
    app.run(debug=True)
