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
    try:
        # Simulated internal check (replace with actual checks e.g., database connectivity, server load)
        # Example: raise Exception("Simulated failure") to simulate an unhealthy service
        service_status = True  # Assume the service is healthy

        if service_status:
            response = jsonify({"status": "healthy"}), 200
        else:
            response = jsonify({"status": "unhealthy"}), 500
    except Exception as e:
        logging.error(f"Internal check failed: {str(e)}")
        response = jsonify({"status": "unhealthy"}), 500

    # Log the response details
    logging.info(f"Response status: {response[1]}, message: {response[0].json}")

    return response
