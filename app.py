from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    # Log the request details
    current_time = datetime.datetime.now()
    ip_address = request.remote_addr
    app.logger.info(f"Timestamp: {current_time}, IP: {ip_address}")

    return jsonify({"status": "healthy"}), 200
