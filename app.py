from flask import Flask, request, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    # Log the request details
    ip_address = request.remote_addr
    timestamp = datetime.now()
    logging.info(f"Received ping at {timestamp} from {ip_address}")

    # Return the response
    response = jsonify({"message": "pong"})
    response.status_code = 200

    # Log the response details
    logging.info(f"Responded at {datetime.now()} with status {response.status_code}")

    return response
