#!/usr/bin/env python
import logging
from flask import Flask
from flask_basicauth import BasicAuth

logging.basicConfig(filename='file.log', filemode='w',level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

basic_auth = BasicAuth(app)

@app.route('/')
@app.route('/hello')  # this route is not working
@app.route('/hello/')
@basic_auth.required
def hello_world():
    logger.info('hello_world called- output: Hello World')
    return 'Hello World!'


@app.route('/hello/<username>') # dynamic route
@basic_auth.required
def hello_user(username):
    # show the user profile for that user
    logger.info('hello_user called- output ' + username)
    return 'Hello %s!\n' % username


if __name__ == '__main__':
    logger.info('Start Demo Flask app')
    app.run(host='0.0.0.0')  # open for everyone
