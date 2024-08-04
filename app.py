from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping")
def ping():
    response = jsonify({"message": "pong"})
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response
