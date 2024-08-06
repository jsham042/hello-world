from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping")
def ping_endpoint():
    current_time = datetime.datetime.now()
    ip_address = request.remote_addr
    app.logger.info(f"Accessed at {current_time} from IP {ip_address}")
    return jsonify({"status": "healthy"}), 200
