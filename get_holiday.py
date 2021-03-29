#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/18 16:29
@Author:  linjinting
@File: get_holiday.py
@Software: PyCharm
"""

import requests
import logging
from utils import f_handler
from utils import get_yesterday_for_str
from load_file import JSON_DATA

logger = logging.getLogger("worker.holiday")
logger.addHandler(f_handler)

def api_holiday(js_data, date):
    # api = 'http://timor.tech/api/holiday/info/'
    url = ""
    try:
        url = js_data['client']['api_holiday'] + date
        res = requests.get(url)
        return res.json()
    except Exception as e:
        logger.error('url[%s], %s' %(url, e))


def is_worker_day(date):
    """

    :param date: str date "2020-02-02"
    :return:
    """
    custom_worker_day = JSON_DATA.get('custom_worker_day', [])
    custom_rest_day = JSON_DATA.get('custom_rest_day', [])
    logger.info("custom_worker_day{%s}" %custom_worker_day)
    logger.info("custom_rest_day{%s}" %custom_rest_day)
    # api = js_date['client']['api_holiday']
    res = api_holiday(JSON_DATA, date)
    if not res:
        return
    logger.info('[api] %s:res %s' % (date, res))

    date_type = res['type']['type']
    if date in custom_rest_day:
        return False
    if date_type in [0, 3] or date in custom_worker_day :
        return True
    return False

def find_before_worker_day(str_date, fmt="%Y-%m-%d"):
    yesterday = get_yesterday_for_str(str_date, fmt) # 获取目标日期的前一天日期
    ret = is_worker_day(yesterday)
    if ret:
        return yesterday
    return find_before_worker_day(yesterday, fmt)



if __name__ == '__main__':
    ret = is_worker_day('2021-05-02')
    print(ret)