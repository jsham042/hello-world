from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping")
def ping():
    # Log the timestamp and requester's IP address
    timestamp = datetime.datetime.now()
    requester_ip = request.remote_addr
    print(f"Timestamp: {timestamp}, IP: {requester_ip}")

    response = jsonify({"message": "pong"})
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    return response
