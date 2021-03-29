#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/18 15:20
@Author:  linjinting
@File: utils.py
@Software: PyCharm
"""

import datetime
import logging
f_handler = logging.FileHandler('worker.log', encoding="utf-8")
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

def get_yesterday():
    """
    获取昨天日期
    :return: str
    """
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    # print(str(yesterday))
    return yesterday.strftime("%Y-%m-%d")

def get_yesterday_for_str(str_date, fmt="%Y-%m-%d"):
    """
    获取昨天日期
    :return: str
    """
    yesterday = get_date_for_str(str_date, fmt) - datetime.timedelta(days=1)
    return str(yesterday)


def get_today_to_str():
    # today = datetime.date.today()
    return str(datetime.date.today())

def get_datetime_for_str(str_date, fmt="%Y-%m-%d"):
    return datetime.datetime.strptime(str_date, fmt)  # 字符串转化为datetime形式

def get_date_for_str(str_date, fmt="%Y-%m-%d"):
    return datetime.datetime.date(get_datetime_for_str(str_date, fmt))  # 字符串转化为date形式

