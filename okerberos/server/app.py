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


token = None
key = b'\xbe?_\xdd\xdb\x02z\xc3\x8b\xf5\xdc\x0b\xdey\xf5\xa0rT\x10\x87>6\x8c\xba\x18Galt*\x1f\xee'
box = nacl.secret.SecretBox(key)
@app.route('/', methods=['GET'])
def index():
    token = request.form['Token']
    print(token)


def run():
    app.run(host='127.0.0.1', port=5002,debug=True)
