from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    # Log the details of the incoming request
    logging.info(f"Received request at /api/ping from {request.remote_addr}")

    # Process the request and prepare the response
    response = jsonify({"status": "ok"}), 200

    # Log the details of the response
    logging.info(f"Response sent: {response}")

    return response
