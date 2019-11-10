from flask import Flask, request
import redis

app = Flask(__name__)

rconn = redis.StrictRedis()


def keygen(key):
    return "token:{key}".format(key=key)

@app.route('/api/register', methods=["POST"])
def register_token():
    userid = request.form['userid']
    token = request.form['token']

    rconn.set(keygen(userid), token)
