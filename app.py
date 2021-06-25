from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from flask_nav import Nav

app = Flask(__name__)
Bootstrap(app)

'''
@app.route('/')
def logs():
    return render_template('login.html')


@app.route('/',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '123456':
        return render_template('index.html')
    else:
        return render_template('login.html',msg='Wrong Username/Password')
'''


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cloudresource')
def cloudresource():
    return  render_template('cloudresource.html')


@app.route('/ipteam')
def ipteam():
    return render_template('ipteam.html')


@app.route('/noc')
def noc():
    return render_template('noc.html')

@app.route('/voiceteam')
def voiceteam():
    return render_template('voiceteam.html')

@app.route('/mobileteam')
def mobileteam():
    return render_template('mobileteam.html')

@app.route('/idc')
def idc():
    return render_template('idc.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/codes')
def codes():
    return render_template('codes.html')

@app.route('/otherteamtemplate')
def otherteamtemplate():
    return render_template('otherteamtemplate.html')

@app.route('/abouts')
def abouts():
    return render_template('abouts.html')


if __name__ == '__main__':
    app.run()
