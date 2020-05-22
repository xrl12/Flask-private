import os
from flask import Flask, request, render_template,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename  # 使用secure_filename会自动校验文件名字


app = Flask(import_name=__name__, template_folder='../templates')

UPLOAD_FOLDER = '../media'
ALLOW_IMG = ['jpg', 'jpeg', 'png', 'gif']


@app.route('/')
def register():
    return render_template('register.html')


@app.route('/upload', methods=['POST'])
def upDown():
    img = request.files.get('img')
    img_name  = img.filename
    if img_name.rsplit('.')[-1] not in ALLOW_IMG:
        ctx = {'error':'图片格式不正对'}
        return render_template('register.html',**ctx)
    name = secure_filename(img_name)
    path = os.path.join(UPLOAD_FOLDER,name)
    img.save(path)
    return redirect(url_for('show',name=name))


@app.route('/show/<name>')
def show(name):
    return send_from_directory(UPLOAD_FOLDER,name)


if __name__ == '__main__':
    app.run(debug=True)
