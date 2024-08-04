from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    start_time = time.time()
    response = jsonify({"status": "healthy"}), 200
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds

    if elapsed_time > 500:
        logging.error(
            f"Performance issue: ping response time exceeded 500ms, actual time {elapsed_time:.2f}ms"
        )

    return response
