from flask import Flask, jsonify

app = Flask(__name__)

# Set the timeout for the response
app.config["RESPONSE_TIMEOUT"] = 300  # Timeout in milliseconds


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/api/ping", methods=["GET"])
def health_check():
    app.logger.info("Accessed /api/ping endpoint")
    return jsonify({"status": "healthy"}), 200
