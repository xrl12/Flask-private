from flask import Flask, render_template

app = Flask(import_name=__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('mecro/mecro.html')

if __name__ == '__main__':
    app.run(debug=True)