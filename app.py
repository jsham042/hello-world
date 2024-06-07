from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from logging.handlers import RotatingFileHandler
import json

app = Flask(__name__)

# Initialize Flask-Limiter
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["5 per minute"],  # Adjust the rate limit as needed
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pingLogger")
handler = RotatingFileHandler("ping.log", maxBytes=10000, backupCount=1)
logger.addHandler(handler)


def log_request(req, res):
    logger.info(
        json.dumps(
            {
                "timestamp": req.date,
                "method": req.method,
                "ip": req.remote_addr,
                "path": req.path,
                "status_code": res.status_code,
            }
        )
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


@app.after_request
def after_request_func(response):
    if request.path == "/ping":
        log_request(request, response)
    return response


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
@limiter.limit("5 per minute")  # Apply rate limiting to the ping endpoint
def ping():
    return "pong"
