import requests
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def send_health_check_request():
    url = "https://api.example.com/health-check"
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time
        return response_time, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed with exception: {e}")
        return None, None


def health_check():
    url = "http://example.com/api/health"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Health check successful: {response.text}")
        else:
            logging.error(
                f"Health check failed with status code {response.status_code}: {response.text}"
            )
    except requests.exceptions.RequestException as e:
        logging.error(f"Health check failed with exception: {e}")


# Scheduler configuration
scheduler = BlockingScheduler()
scheduler.add_job(health_check, "interval", minutes=5)

if __name__ == "__main__":
    logging.info("Starting health check scheduler.")
    scheduler.start()
