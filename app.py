from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping")
def ping():
    response = make_response(jsonify({"message": "pong"}), 200)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Content-Type"] = "application/json"
    return response
