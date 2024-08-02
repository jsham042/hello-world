from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/ping", methods=["GET"])
def ping():
    current_time = (
        datetime.utcnow().isoformat() + "Z"
    )  # ISO 8601 format with Zulu time indicator
    return jsonify({"status": "pong", "timestamp": current_time}), 200


if __name__ == "__main__":
    app.run(debug=True)
