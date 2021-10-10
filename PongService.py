from flask import Flask
from flask_httpauth import HTTPDigestAuth
import random

app = Flask(__name__)

auth = HTTPDigestAuth()

user = {
    "vcu": "rams"
}


@auth.get_password
def get_pw(username):
    if username in user:
        return user.get(username)
    return None
