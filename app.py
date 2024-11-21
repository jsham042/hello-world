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
    start_time = datetime.now()
    logging.info(f"Request to /api/ping at {start_time.isoformat()}")
    response = jsonify({"status": "healthy"})
    response_time = datetime.now()
    logging.info(
        f"Response status: {response.status_code} at {response_time.isoformat()}"
    )
    return response, 200
