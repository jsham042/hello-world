from flask import Flask, jsonify
import datetime
import os
import platform

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    timestamp = datetime.datetime.now().isoformat()
    uptime = os.popen("uptime").read().strip()
    version = platform.python_version()
    response = {
        "status": "success",
        "message": "pong",
        "timestamp": timestamp,
        "uptime": uptime,
        "version": version,
    }
    return jsonify(response), 200
