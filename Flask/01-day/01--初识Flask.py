from flask import Flask

app = Flask(__name__)


@app.route('/center')
def center():
    return '哈喽啊'


if __name__ == '__main__':
    app.run()
