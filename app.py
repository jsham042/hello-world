from flask import Flask, jsonify, request
import logging

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    logging.info(f"Request received: {request}")
    response = jsonify({"status": "ok"})
    logging.info(f"Response sent: {response.get_json()}")
    return response, 200
