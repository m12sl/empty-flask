__author__ = 'm12sl'
from flask import Flask

app = Flask(__name__)
app.config.from_object('app.config')

@app.route('/')
def index():
    return 'Hello flask!'