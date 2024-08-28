from flask import Flask, jsonify
import logging
from datetime import datetime
import time

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    start_time = time.time()  # Start timing

    # Log the request details
    logging.info(f"Request to /api/ping at {datetime.now()} - Method: GET")

    response = jsonify({"status": "ok"})
    response_time = (
        time.time() - start_time
    ) * 1000  # Calculate response time in milliseconds

    # Log the response time
    logging.info(f"Response time for /api/ping: {response_time:.2f} ms")

    return response, 200
