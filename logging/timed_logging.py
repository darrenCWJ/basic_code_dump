import logging
import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
"""
second (s)
minute (m)
hour (h)
day (d)
w0-w6 (weekday, 0=Monday)
midnight
"""

handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)