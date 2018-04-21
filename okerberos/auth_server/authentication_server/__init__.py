""" Initializes and configures the flask app / DOM """
import sys
from flask import Flask
from flask_restful import Api
from mongoengine import *
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
rest_api = Api(app)

import authentication_server.api.endpoint
rest_api.add_resource(authentication_server.api.endpoint.OAuth_Endpoint, '/login')