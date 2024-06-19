from flask import Flask, jsonify
import logging

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    try:
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        logging.error(f"Internal server error: {e}")
        return jsonify({"error": "Internal server error"}), 500
