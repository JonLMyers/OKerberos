from flask import jsonify, request,  Flask , render_template
from flask_restful import Resource, reqparse
import os
import json
import requests
import sha3
import base58
import base64
import nacl.secret
import nacl.utils
from nacl.encoding import Base64Encoder


app = Flask(__name__)
app.config.from_pyfile('config.py')


token = { }

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['Username']
    password = request.form['Password']

    target = 'http://127.0.0.1:5001/login'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'username': username, 'password': password}
    r = requests.post(target, data=json.dumps(data), headers=headers)
    print(r.status_code, r.reason)
    print(r.text)
    data = json.loads(r.text)
    token['Token'] = data['Token']
    return "retrieved Token!"

@app.route('/forwardtoken', methods=['GET'])
def forwardtoken():
        print(token)
        target = 'http://127.0.0.1:5002/'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {"echo" : "Hello",  "Token" : token["Token"]}
        r = requests.post(target, data=json.dumps(data), headers=headers)
        return r.text





def run():
    app.run(debug=True)
