from flask import Flask, jsonify
import socket

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    try:
        # Check if the host can be resolved to an IP, simulating a basic connectivity check
        socket.gethostbyname("localhost")
        health_status = "healthy"
        return jsonify({"status": health_status}), 200
    except Exception:
        return jsonify({"status": "unhealthy"}), 500
