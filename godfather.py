import schedule
import time
from control.telegram_bot import run_bot

def job():
    print("Scheduled job running...")

schedule.every(10).minutes.do(job)

if __name__ == "__main__":
    run_bot()
    while True:
        schedule.run_pending()
        time.sleep(1)
