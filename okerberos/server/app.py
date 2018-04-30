from flask import jsonify, request,  Flask
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



key = b'\xbe?_\xdd\xdb\x02z\xc3\x8b\xf5\xdc\x0b\xdey\xf5\xa0rT\x10\x87>6\x8c\xba\x18Galt*\x1f\xee'
box = nacl.secret.SecretBox(key)
@app.route('/', methods=['POST'])
def index():
    print("verifying token")
    data = request.get_json()
    if "Token" in data:
        token = data["Token"]
    else:
        return "Unathorized"


    print(token.encode("utf8"))
    cipher_text = box.decrypt(token.encode("utf8"), encoder=Base64Encoder)
    print(cipher_text)

    return data['echo']
def run():
    app.run(host='127.0.0.1', port=5002,debug=True)
