from flask import Flask

app = Flask(import_name=__name__)


@app.route('/')
def index():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return '你好啊'

if __name__ == '__main__':
    app.run(debug=True)

