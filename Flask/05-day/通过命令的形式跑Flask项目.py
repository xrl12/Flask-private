from flask import Flask
from flask_script import Manager

app = Flask(import_name=__name__)

manage = Manager(app)


if __name__ == '__main__':
    manage.run()