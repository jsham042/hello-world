from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    response = jsonify({"status": "ok"})
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response
