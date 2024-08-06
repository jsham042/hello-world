from flask import Flask, jsonify, request
import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["100 per minute"])


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping")
@limiter.limit("100 per minute")
def ping_endpoint():
    current_time = datetime.datetime.now()
    ip_address = request.remote_addr
    app.logger.info(f"Accessed at {current_time} from IP {ip_address}")
    return jsonify({"status": "healthy"}), 200
