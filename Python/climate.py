from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/index/')
def hello_world():
    return render_template('index.html')
    #return '<h1>Climate Inc. Version {}</h1>'.format(version)
@app.route('/index/urmomgay/')
def hoi():
    return '<h1> urmomgay </h1>'