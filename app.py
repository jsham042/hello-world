from flask import Flask, jsonify, request
import logging
from datetime import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up rate limiting
limiter = Limiter(app, key_func=get_remote_address, default_limits=["100 per minute"])


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
@limiter.limit("100/minute")  # Apply rate limiting to this endpoint
def ping_endpoint():
    # Log the request details
    ip_address = request.remote_addr
    timestamp = datetime.now().isoformat()
    logging.info(f"Request from {ip_address} at {timestamp}")

    return jsonify({"status": "healthy"}), 200
