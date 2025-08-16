from __future__ import annotations

import os
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

from manage import run_once

load_dotenv()

TZ = os.getenv("TIMEZONE", "UTC")


sched = BlockingScheduler(timezone=TZ)


@sched.scheduled_job("interval", minutes=60)
def job():
    print("Running scheduled job...")
    run_once(int(os.getenv("MAX_ITEMS_PER_RUN", "50")))


if __name__ == "__main__":
    sched.start()
