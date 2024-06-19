from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    # Perform an internal check
    service_status = True  # This is a simple simulation of an internal check

    if service_status:
        return jsonify({"message": "Service is operational"}), 200
    else:
        return jsonify({"message": "Service is not operational"}), 503
