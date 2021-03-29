#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/18 15:11
@Author:  linjinting
@File: query.py
@Software: PyCharm
"""

import logging
import requests
from utils import f_handler
from load_file import JSON_DATA

logger = logging.getLogger('worker.query')
logger.addHandler(f_handler)


def yesterday_worker_time(name, starDate, endData):
    try:
        url = JSON_DATA['client']['api_reqworktime']
        headers = {'Content-Type': 'application/json'}
        json_data = {
            "username": name,
            "startworkdate": starDate,
            "endworkdate": endData
        }
        response = requests.post(url, json=json_data, headers=headers)
        return response.json()
    except Exception as e:
        logger.error(e)
        return dict()


def get_names_for_group(starDate, endData):
    group_names = JSON_DATA.get('names_map', [])
    empty_names = list()
    for name in group_names:
        res = yesterday_worker_time(name, starDate, endData)
        logger.info("query:%s, response:%s" % (name, res))
        if 0 == res.get('sumtimelong', 0):
            empty_names.append(name)

    return empty_names


if __name__ == '__main__':
    empty_names = get_names_for_group("2021-03-18", "2021-03-18")
    logger.info("empty_names:{%s}" % empty_names)
