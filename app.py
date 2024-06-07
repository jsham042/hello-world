from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Initialize Flask-Limiter
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute"],  # Adjust the rate limit as needed
)


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
@limiter.limit("5 per minute")  # Apply rate limiting to the ping endpoint
def ping():
    return "pong"
