from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/ping", methods=["GET"])
def ping():
    app.logger.info(f"Timestamp: {datetime.now()}, Status: 200")
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run()
