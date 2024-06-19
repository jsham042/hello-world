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
def health_check():
    # Log the timestamp and IP address of the requester
    ip_address = request.remote_addr
    timestamp = datetime.now().isoformat()
    logging.info(f"Health check accessed at {timestamp} from IP {ip_address}")

    return jsonify({"status": "healthy"}), 200
