from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    try:
        # Simulate a health check
        # In a real-world scenario, you would check database connections, external services, etc.
        health_status = "healthy"
        return jsonify({"status": health_status}), 200
    except Exception:
        return jsonify({"status": "unhealthy"}), 500
