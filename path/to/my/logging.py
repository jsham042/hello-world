import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="request_log.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def log_request(request_info):
    """
    Logs information about a request to the ping endpoint.

    Parameters:
    request_info (dict): A dictionary containing information about the request such as timestamp, IP address, endpoint accessed, and outcome.
    """
    # Extracting information from the request_info dictionary
    timestamp = request_info.get(
        "timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    ip_address = request_info.get("ip_address", "Unknown IP")
    endpoint = request_info.get("endpoint", "Unknown Endpoint")
    outcome = request_info.get("outcome", "Unknown Outcome")

    # Formatting the log message
    log_message = f"Timestamp: {timestamp}, IP Address: {ip_address}, Endpoint: {endpoint}, Outcome: {outcome}"

    # Logging the request information
    logging.info(log_message)


# Example usage
if __name__ == "__main__":
    # Example request information
    request_info_example = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": "192.168.1.1",
        "endpoint": "/ping",
        "outcome": "Success",
    }

    # Logging the example request
    log_request(request_info_example)
