from flask import Flask, jsonify, request
import datetime
import time
import logging

app = Flask(__name__)

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)


@app.before_request
def before_request_logging():
    if request.path == "/api/ping":
        request.start_time = datetime.datetime.now()


@app.after_request
def after_request_logging(response):
    if request.path == "/api/ping":
        end_time = datetime.datetime.now()
        duration = (end_time - request.start_time).total_seconds()
        app.logger.info(
            f"Request to {request.path} took {duration} seconds and returned status code {response.status_code}"
        )
    return response


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    # Start time measurement
    start_time = time.perf_counter()

    # Simulate response
    response = jsonify({"status": "ok"}), 200

    # End time measurement
    end_time = time.perf_counter()
    duration = (end_time - start_time) * 1000  # Convert to milliseconds

    # Log the duration and check if it meets the performance requirement
    if duration > 300:
        app.logger.warning(f"Health check exceeded 300ms: {duration}ms")
    else:
        app.logger.info(f"Health check within acceptable duration: {duration}ms")

    return response
