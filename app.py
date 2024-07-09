from flask import Flask, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    # Log the request with timestamp
    logging.info(f"Request to /api/ping at {datetime.now().isoformat()}")
    response = jsonify({"status": "healthy"})
    # Log the response status
    logging.info(
        f"Response status: {response.status_code} at {datetime.now().isoformat()}"
    )
    return response, 200
