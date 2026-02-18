import requests
import time
import threading
from datetime import datetime

URL = "https://serenify-backend-25s5.onrender.com/health"

INTERVALS = {
    "5_min": 5 * 60,
    "7_min": 7 * 60,
    "10_min": 10 * 60,
    "30_min": 30 * 60,
}

def ping_service(name, interval):
    while True:
        try:
            response = requests.get(URL, timeout=10)
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{name} ping → Status: {response.status_code}"
            )
        except Exception as e:
            print(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{name} ping → ERROR: {e}"
            )

        time.sleep(interval)

if __name__ == "__main__":
    for name, interval in INTERVALS.items():
        thread = threading.Thread(
            target=ping_service,
            args=(name, interval),
            daemon=True
        )
        thread.start()

    print("🚀 Health pinger started for 5, 7, 10, and 30 minutes intervals.")
    
    while True:
        time.sleep(60)
