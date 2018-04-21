import json
import requests
import hashlib
from Crypto.Cipher import AES
from flask import jsonify, request
from flask_restful import Resource, reqparse
from authentication_server import rest_api

class OAuth_Endpoint(Resource):
    def post(self):
        data = parser.parse_args()
        m = hashlib.sha256()
        username = data['username']
        password = data['password']
        password_hash = m.update(password).digest()

        if username == '' or password == '':
            return{'Auth': 'Fail', 'Token': ''}, 500

        target = 'http://127.0.0.1:5002/login'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': username, 'password': password}
        r = requests.post(target, data=json.dumps(data), headers=headers)
        print(r.status_code, r.reason)
        print(r.text)
        data = json.loads(r.text)
        status = data['Auth']
        token = data['Token']
        print(status)        

        if status == 'success' and token != '':
            encryption_suite = AES.new('I_Love_Candy', AES.MODE_CBC, 'Candy_Is_Good')
            cipher_text = encryption_suite.encrypt(token)
            unencrypt_json = {'Auth': 'Success', 'Token': cipher_text}
            encryption_suite = AES.new(password_hash, AES.MODE_CBC, 'Candy_Is_Good')
            cipher_text = encryption_suite.encrypt(cipher_text)
            return{'Token': cipher_text}, 200


        else:
            return{'Error': 'Invalid Arguments'}, 500
