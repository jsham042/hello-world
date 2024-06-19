from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    # Log the request details
    logging.info(f"Received request at /ping from {request.remote_addr}")

    # Perform an internal check
    service_status = True  # This is a simple simulation of an internal check

    if service_status:
        response = jsonify({"message": "Service is operational"}), 200
    else:
        response = jsonify({"message": "Service is not operational"}), 503

    # Log the response details
    logging.info(f"Response status: {response[1]}, message: {response[0].json}")

    return response
