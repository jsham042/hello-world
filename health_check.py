import requests
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


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
