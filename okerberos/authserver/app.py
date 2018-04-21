""" Runs the server """

import sys
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from  okerberos.authserver.endpoint import OAuth_Endpoint

app = Flask(__name__)

CORS(app)

rest_api = Api(app)
rest_api.add_resource(OAuth_Endpoint, '/login')

def run():
    app.run(host='127.0.0.1', port=5001)
