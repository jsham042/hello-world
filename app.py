from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    try:
        # Simulate a check for the operational status of the service
        # This is a placeholder for actual operational checks
        service_operational = (
            True  # This should be replaced with actual health check logic
        )

        if service_operational:
            return jsonify({"status": "healthy"}), 200
        else:
            return (
                jsonify({"status": "unhealthy", "description": "Service is down"}),
                503,
            )
    except Exception as e:
        return jsonify({"status": "unhealthy", "description": str(e)}), 503
