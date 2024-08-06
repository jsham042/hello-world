from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping")
def ping_endpoint():
    return jsonify({"status": "healthy"}), 200
