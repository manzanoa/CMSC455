from flask import Flask, jsonify, requests
from flask_httpauth import HTTPDigestAuth
import time


app = Flask(__name__)

auth = HTTPDigestAuth()

user = {
    "vcu": "rams"
}

number = requests.get(*insert url here*, auth=HTTPDigestAuth('vcu', 'rams'))

@auth.get_password
def get_pw(username):
    if username in user:
        return user.get(username)
    return None


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
