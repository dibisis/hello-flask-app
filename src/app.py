#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'


@app.route('/hello/<username>')  # api for vars
def hello_user(username):
    return 'Hello you, %s!\n' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # open for everyone
