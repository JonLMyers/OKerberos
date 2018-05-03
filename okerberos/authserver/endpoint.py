from flask import jsonify, request, Flask
from flask_restful import Resource, reqparse
from nacl.public import PrivateKey, SealedBox
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

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'



class OAuth_Endpoint(Resource):

    target = 'https://127.0.0.1/token.php'
    key = b'\xbe?_\xdd\xdb\x02z\xc3\x8b\xf5\xdc\x0b\xdey\xf5\xa0rT\x10\x87>6\x8c\xba\x18Galt*\x1f\xee'
    box = nacl.secret.SecretBox(key)
    client_id = "testclient"
    client_secret = "testpass"
    access_token_data = {"grant_type": "client_credentials","client_id": client_id,"client_secret": client_secret}
    privatekey = None
    publickey = None
    privatekey = PrivateKey.generate()

    #key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    def post(self):
        data = request.get_json()
        decoded_encrypted_msg = base64.b64decode(data['message'].encode('utf8'))
        unsealed_box = SealedBox(self.privatekey)
        decoded_decrypted_msg = unsealed_box.decrypt(decoded_encrypted_msg)

        data = json.loads(decoded_decrypted_msg.decode())
        username = data['username']
        password = data['password']
        print(data)

        hash_object = sha3.sha3_256(password.encode())
        password_hash = hash_object.digest()
        if username == '' or password == '':
            return{'Auth': 'Fail', 'Token': ''}, 500
        pwkey = nacl.secret.SecretBox(password_hash)
        oauth_resp = requests.post(self.target, data=self.access_token_data, verify=False, allow_redirects=False)
        access = json.loads(oauth_resp.text)

        token = access['access_token']

        if requests.codes.ok == oauth_resp.status_code and token != '':
            cipher_text = self.box.encrypt(token.encode(), encoder=Base64Encoder)
            encoded_ciphertext = cipher_text.decode('utf8')
            unencrypt_json = {'Auth': 'Success', 'Token': encoded_ciphertext }
            print(unencrypt_json)
            encrypted_message = pwkey.encrypt(json.dumps(unencrypt_json).encode(), encoder=Base64Encoder)
            return {'message' : encrypted_message.decode('utf8')}, 200
        else:
            return{'Error': 'Invalid Arguments'}, 500

    def get(self):
        # RSA modulus length must be a multiple of 256 and >= 1024
        self.publickey = self.privatekey.public_key.encode(encoder=nacl.encoding.Base64Encoder()).decode('utf-8')
        return {'Pub_Key': self.publickey}, 200
