from flask import Flask, g

app = Flask(__name__)

@app.before_request
def before_request():
    print('before_request!')
    g.str = '한글'

@app.route('/')
def index():
    return 'index' + getattr(g, 'str', '111')