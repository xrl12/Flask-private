from flask import Flask, g

app = Flask(import_name=__name__)


@app.route('/')
def index():
    g.age = 12
    show()
    return '你好啊'


def show():
    print(g.age)


if __name__ == '__main__':
    app.run()
