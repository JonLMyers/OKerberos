from flask import Flask, render_template
from flask_restful import Resource, reqparse
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = parser.parse_args()
    username = data['username']
    password = data['password']

    target = 'http://127.0.0.1:5001/login'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'username': username, 'password': password}
    r = requests.post(target, data=json.dumps(data), headers=headers)
    print(r.status_code, r.reason)
    print(r.text)
    data = json.loads(r.text)
    print(data)
app.run(Debug=True)