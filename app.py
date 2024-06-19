from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


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
    return jsonify({"status": "ok"}), 200
