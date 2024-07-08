from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def health_check():
    # Log the request details
    ip_address = request.remote_addr
    timestamp = datetime.datetime.now()
    print(f"Timestamp: {timestamp}, IP Address: {ip_address}")

    return jsonify({"status": "healthy"}), 200
