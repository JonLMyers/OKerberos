import requests

SERVER_URI =  "http://localhost:3456"

def postCredentials(credentials):
    response = requests.post(SERVER_URI,credentials.to_dict())
