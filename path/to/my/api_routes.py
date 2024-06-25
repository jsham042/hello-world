from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/ping")
def ping():
    return jsonify({"message": "pong"}), 200


if __name__ == "__main__":
    app.run(debug=True)
