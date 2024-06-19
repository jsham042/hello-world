from flask import Flask, jsonify, request
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
    # Log the timestamp and IP address of the requester
    ip_address = request.remote_addr
    timestamp = datetime.now().isoformat()
    logging.info(f"Accessed /api/ping - IP: {ip_address}, Timestamp: {timestamp}")

    return jsonify({"status": "healthy"}), 200
