from flask import Flask, request, jsonify, make_response
from functools import wraps
import time

app = Flask(__name__)

# Define a simple in-memory "database" for tracking request counts
# In a production scenario, consider using a more persistent storage mechanism
request_counts = {}
WINDOW_SIZE = 60  # 1 minute window
MAX_REQUESTS = 5  # Max requests per window per user


def rate_limiter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Identify user uniquely, here using IP for simplicity. In real scenarios, use a more robust method.
        user_identifier = request.remote_addr

        current_time = int(time.time())
        window_start = current_time - WINDOW_SIZE

        # Initialize user's request count history if not present
        if user_identifier not in request_counts:
            request_counts[user_identifier] = []

        # Filter out requests outside the current window
        requests_within_window = [
            timestamp
            for timestamp in request_counts[user_identifier]
            if timestamp > window_start
        ]

        # Update the request count history with the current request
        requests_within_window.append(current_time)
        request_counts[user_identifier] = requests_within_window

        # Check if the request count within the window exceeds the limit
        if len(requests_within_window) > MAX_REQUESTS:
            # Too many requests; deny the request
            return make_response(jsonify({"error": "Rate limit exceeded"}), 429)

        # Proceed with the request
        return func(*args, **kwargs)

    return wrapper


@app.route("/ping", methods=["GET"])
@rate_limiter
def ping():
    return jsonify({"message": "pong"})


if __name__ == "__main__":
    app.run(debug=True)
