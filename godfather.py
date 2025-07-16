import schedule
import time
import threading
from control.telegram_bot import run_bot

def job():
    print("Scheduled job running...")

def run_scheduler():
    schedule.every(10).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Run the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

    # Start the Telegram bot (this blocks the main thread)
    run_bot()
