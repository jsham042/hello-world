from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up rate limiter
limiter = Limiter(app, key_func=get_remote_address, default_limits=["60 per minute"])


@app.route("/")
def hello_world():
    logging.info(f"Request to root from {request.remote_addr} at {request.date}")
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
@limiter.limit("60/minute")
def ping():
    logging.info(f"Request to /ping from {request.remote_addr} at {request.date}")
    return jsonify({"message": "pong"})
