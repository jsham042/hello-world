import requests
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import schedule

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_response(response_time, status_code):
    logging.info(f"Response time: {response_time} seconds, Status code: {status_code}")


def send_health_check_request():
    url = "https://api.example.com/health-check"
    try:
        start_time = time.time()
        response = requests.get(url)
        response_time = time.time() - start_time
        log_response(response_time, response.status_code)
        return response_time, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed with exception: {e}")
        return None, None


def check_response(response):
    try:
        data = response.json()
        if response.status_code == 200 and data.get("status") == "ok":
            return True
    except ValueError:
        logging.error("Invalid JSON response")
    return False


def health_check():
    url = "http://example.com/api/health"
    try:
        response = requests.get(url)
        if check_response(response):
            logging.info(f"Health check successful: {response.text}")
        else:
            logging.error(
                f"Health check failed with status code {response.status_code}: {response.text}"
            )
    except requests.exceptions.RequestException as e:
        logging.error(f"Health check failed with exception: {e}")


def schedule_health_checks():
    schedule.every(5).minutes.do(send_health_check_request)
    while True:
        schedule.run_pending()
        time.sleep(1)


# Scheduler configuration
scheduler = BlockingScheduler()
scheduler.add_job(health_check, "interval", minutes=5)

if __name__ == "__main__":
    logging.info("Starting health check scheduler.")
    scheduler.start()
    schedule_health_checks()
