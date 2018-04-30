import requests, json
from flask import Flask, render_template, request
from flask_restful import Resource, reqparse

app = Flask(__name__)
app.config.from_pyfile('config.py')


token = None

@app.route('/', methods=['GET'])
def index():
    token = request.form['Token']




def run():
    app.run(host='127.0.0.1', port=5002,debug=True)
