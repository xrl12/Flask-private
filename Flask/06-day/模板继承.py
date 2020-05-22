from flask import Flask,render_template
from flask_script import Manager

app = Flask(import_name=__name__,template_folder='../templates')

manager = Manager(app)

@app.route('/')
def index():
    return render_template('inherit/index1.html')

if __name__ == '__main__':
    manager.run()