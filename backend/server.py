import logging

import flask
from flask import request
from flask_cors import CORS, cross_origin
import  myregister
import login


app = flask.Flask(__name__)

CORS(app)


@app.route('/register/', methods = ['GET', 'POST'])
@cross_origin(origin='*')
def registerr():
    email = request.args.get("email")
    password = request.args.get("password")
    #print(email)
    #print(password)

    return myregister.register(email, password)


@app.route('/login', methods = ['GET', 'POST'])
@cross_origin(origin='*')
def loginn():

    email=request.args.get("email")
    password=request.args.get("password")
    return login.login(email,password)


if __name__ == '__main__':
#pip install pyopenssl
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
