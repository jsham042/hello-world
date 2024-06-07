from flask import Flask, request, jsonify

app = Flask(__name__)


def authenticate():
    auth_token = request.headers.get("Authorization")
    if auth_token != "Bearer valid_token":
        return jsonify({"error": "Unauthorized"}), 401


@app.before_request
def before_request_func():
    if request.path == "/ping":
        response = authenticate()
        if response:
            return response


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    return "pong"
