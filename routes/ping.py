from flask import Flask, jsonify
from datetime import datetime
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, default_limits=["60 per minute"])


@app.route("/ping", methods=["GET"])
@limiter.limit("60 per minute")
def ping():
    current_time = datetime.utcnow().isoformat() + "Z"
    return jsonify({"status": "pong", "timestamp": current_time}), 200


if __name__ == "__main__":
    app.run(debug=True)
