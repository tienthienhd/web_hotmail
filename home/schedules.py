import logging
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from home.models import *

log = logging.getLogger("core")

def start_all_schedules():
    scheduler = BackgroundScheduler()
    scheduler.configure(timezone=timezone.get_current_timezone())
    # scheduler.add_job(_sync_data_blacklist, trigger='cron',
    #                   year='*', month='*', week='*', day='*', day_of_week='*',
    #                   hour=0, minute=0, second=0)
    #                   # hour='02', minute='34', second='00')
    # scheduler.start()
