from flask import Flask, request
from security import verify_token
from rate_limiting import rate_limiter
from logging import log_request

app = Flask(__name__)


# Middleware for rate limiting
@app.before_request
def before_request_func():
    rate_limiter(request)


@app.route("/ping", methods=["GET"])
def ping():
    # Verify token
    if not verify_token(request):
        return "Unauthorized", 401

    # Log the request
    log_request(request)

    # Return pong response
    return "pong", 200


if __name__ == "__main__":
    app.run(debug=True)
