#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/18 16:06
@Author:  linjinting
@File: run.py
@Software: PyCharm
"""
import logging
from get_holiday import is_worker_day, find_before_worker_day
from query_worker_time import get_names_for_group
from push_WXWork import push_message
from utils import get_yesterday, get_today_to_str
from utils import f_handler
from load_file import JSON_DATA

from celery_app import app



LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s:%(lineno)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)
logger = logging.getLogger('worker.run')
logger.addHandler(f_handler)


def exclude_extra_names(source_names, extra_names):
    for extra in extra_names:
        if extra in source_names:
            source_names.remove(extra)
    return source_names

@app.task(name="run.test")
def test():
    print("celery task test")

@app.task(name="run.run")
def run():
    logger.info('start running')
    today = get_today_to_str()
    ret = is_worker_day(today)
    if ret:
        # yesterday = get_yesterday()
        worker_day = find_before_worker_day(today)
        names = get_names_for_group(worker_day, worker_day)
        names = exclude_extra_names(names, JSON_DATA.get('extra_names', []))
        logger.info(names)
        if names:
            push_message(names, worker_day)
        logger.info('end')
    else:
        logger.info('today is not worker day, exit!!!')


if __name__ == '__main__':
    run()
    # aa = [u"马景松", u"闵和矗", u"易尊忠"]
    # print str(aa).decode('unicode-escape')