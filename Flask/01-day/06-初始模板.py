from flask import Flask, render_template

app = Flask(import_name=__name__, template_folder='../templates')


@app.route('/')
def index():
    ctx = {
        'happys': ['吃饭', '喝酒', '打豆豆'],
        'gender': '男',
        'name': '小徐'
    }
    return render_template('index.html', **ctx)


# 自定义过滤器
def show(value):
    return str(value) + '你好啊'


app.jinja_env.filters['show'] = show

if __name__ == '__main__':
    app.run(debug=True)
