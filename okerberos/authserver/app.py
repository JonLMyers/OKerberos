""" Runs the server """

import sys
from flask import Flask
from flask_restful import Api
from mongoengine import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import authentication_server.api.endpoint

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
rest_api = Api(app)

rest_api.add_resource(authentication_server.api.endpoint.OAuth_Endpoint, '/login')

def run():
    app.run(host='127.0.0.1', port=5001)
