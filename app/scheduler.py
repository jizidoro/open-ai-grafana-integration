import schedule
import time
from app.fetch_openai_stats import fetch_stats
from app.push_to_influxdb import push_to_influxdb

def job():
    stats = fetch_stats()
    push_to_influxdb(stats)

def start_scheduler():
    schedule.every(5).minutes.do(job)  # Adjust interval based on config

    while True:
        schedule.run_pending()
        time.sleep(1)