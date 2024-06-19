from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    # Log the timestamp and IP address of the requester
    timestamp = datetime.datetime.now()
    ip_address = request.remote_addr
    print(f"Timestamp: {timestamp}, IP Address: {ip_address}")

    return jsonify({"status": "healthy"}), 200
