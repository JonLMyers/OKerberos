from flask import jsonify, request,  Flask , render_template
from flask_restful import Resource, reqparse
import os
import json
import requests
import sha3
import base58
import base64
import colors

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
    userlog , passlog  = colors.color("{}={}".format('username', username), fg='blue') , colors.color("{}={}".format('pass', password), fg='red')
    app.logger.info(userlog + " " + passlog)

    data = json.loads(r.text)
    hash_object = sha3.sha3_256(password.encode())
    password_hash = hash_object.digest()
    pwkey = nacl.secret.SecretBox(password_hash)
    decrypted_respo = pwkey.decrypt(data['message'].encode('utf8'), encoder=Base64Encoder)
    dumped_respo = json.loads(decrypted_respo.decode('utf8'))

    app.logger.info(colors.color("{}={}".format('Descrpted response', dumped_respo),fg='red'))

    token["Token"] = dumped_respo["Token"]
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
