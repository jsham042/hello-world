from flask import Flask, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    # Log the request details
    logging.info(f"Request to /api/ping at {datetime.now()} - Method: GET")
    return jsonify({"status": "ok"}), 200
