from datetime import timedelta

import redis
from flask import Flask, session, redirect, url_for
from flask_session import Session

app = Flask(import_name=__name__)

app.config['SECRET_KEY'] = 'asdfasfsadfasdfasdfa'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=10)


@app.route('/')
def index():
    uid = session.get('uid')
    if uid:
        return uid
    return '你好啊'


# 保存session
@app.route('/login')
def login():
    # session.permanent = True
    session['uid'] = 'xxx'
    session['age'] = '11'
    return redirect(url_for('index'))


# 删除session
@app.route('/del')
def del_session():
    # session.pop('uid')  # 删除指定session
    # del session['uid']  # 删除指定session
    session.clear()  # 清空session
    return redirect(url_for('index'))


# 把session放在redis里面
f_session = Session()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'laowangaigebi'  # 加密的密钥
app.config['SESSION_USE_SIGNER'] = True  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
app.config['PERMANENT_SESSION_LIFETIME'] = 7200  # 失效时间 秒
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', db=0)  # redis数据库连接


@app.route('/redis')
def redis():
    session['uid'] = 'redis'
    return 'nihao'


# 绑定flask的对象
f_session.init_app(app)
if __name__ == '__main__':
    app.run(debug=True)
