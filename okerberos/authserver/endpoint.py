from flask import jsonify, request
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

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'



class OAuth_Endpoint(Resource):

    target = 'http://127.0.0.1/token.php'
    key = b'\xbe?_\xdd\xdb\x02z\xc3\x8b\xf5\xdc\x0b\xdey\xf5\xa0rT\x10\x87>6\x8c\xba\x18Galt*\x1f\xee'
    box = nacl.secret.SecretBox(key)
    client_id = "testclient"
    client_secret = "testpass"
    access_token_data = {"grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret}
    #key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        hash_object = sha3.sha3_256(password.encode())
        password_hash = hash_object.hexdigest()
        if username == '' or password == '':
            return{'Auth': 'Fail', 'Token': ''}, 500

        oauth_resp = requests.post(self.target, data=self.access_token_data, verify=False, allow_redirects=False)
        access = json.loads(oauth_resp.text)

        token = access['access_token']

        if requests.codes.ok == oauth_resp.status_code and token != '':

            print(token)
            cipher_text = self.box.encrypt(token.encode(), encoder=Base64Encoder)
            print("Cipher Text" , cipher_text)
            encoded_ciphertext = cipher_text.decode('utf8')
            unencrypt_json = {'Auth': 'Success', 'Token': encoded_ciphertext }
            return unencrypt_json, 200
        else:
            return{'Error': 'Invalid Arguments'}, 500
