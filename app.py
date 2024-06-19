from flask import Flask, jsonify, request
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


# API Documentation
# -----------------
# Endpoint: /
# Purpose: Returns a greeting message.
# Request format: GET request.
# Response: Plain text response.
# Example response: "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"


# API Documentation
# -----------------
# Endpoint: /api/ping
# Purpose: Checks the health of the API.
# Request format: GET request.
# Response: JSON response indicating the status.
# Example response: {"status": "healthy"}
@app.route("/api/ping", methods=["GET"])
def ping():
    # Log the timestamp and IP address of the requester
    ip_address = request.remote_addr
    timestamp = datetime.now().isoformat()
    logging.info(f"Accessed /api/ping - IP: {ip_address}, Timestamp: {timestamp}")

    return jsonify({"status": "healthy"}), 200
