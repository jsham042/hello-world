from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def ping():
    return jsonify(status=True, message="Service operational"), 200


def check_system_health():
    # Example checks (these would be replaced with actual checks in a real application)
    database_status = {"status": True, "message": "Database connection successful"}
    external_api_status = {"status": True, "message": "External API reachable"}

    health_check_results = {
        "database": database_status,
        "external_api": external_api_status,
    }

    return health_check_results


@app.route("/api/health", methods=["GET"])
def health():
    health_status = check_system_health()
    all_good = all(component["status"] for component in health_status.values())
    status_code = 200 if all_good else 503
    return jsonify(health_status), status_code
