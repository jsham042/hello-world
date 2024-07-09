from flask import Flask, jsonify, request
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    """
    API Endpoint: /api/ping
    Method: GET
    Sample Request: GET /api/ping
    Sample Response: {"status": "ok"}

    This endpoint provides a simple health check to verify that the API is operational.
    When accessed, it logs the request details including timestamp, requester's IP, and method used,
    and returns a JSON response indicating the status is 'ok'.
    """
    # Log the request details
    logging.info(
        f"Timestamp: {datetime.now()}, IP: {request.remote_addr}, Method: GET, Endpoint: /api/ping"
    )
    return jsonify({"status": "ok"}), 200
