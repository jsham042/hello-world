from flask import Flask, jsonify, request, abort

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def check_auth(token):
    # Placeholder for token validation logic
    # In a real-world scenario, replace this with actual validation logic
    return token == "secret-token"


@app.route("/api/ping", methods=["GET"])
def ping():
    # Retrieve the token from the request headers
    token = request.headers.get("Authorization")

    # Check if the token is valid
    if not check_auth(token):
        # If the token is invalid, return 401 Unauthorized
        abort(401)

    # If the token is valid, proceed to return the status
    return jsonify(status="healthy"), 200
