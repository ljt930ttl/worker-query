#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/18 15:51
@Author:  linjinting
@File: push_WXWork.py
@Software: PyCharm
"""

import logging
import requests
import json
from utils import f_handler
from load_file import JSON_DATA
logger = logging.getLogger('worker.push')
logger.addHandler(f_handler)

# names_map = { "林进庭":"linjinting", "闵和矗":"minhechu", "邱志基":"qiuzhiji", "马景松":"majingsong", "易尊忠":"yizunzhong"}

def push_message(names, date):
    webhook = JSON_DATA['client']['api_webhook']
    names_map = JSON_DATA.get('names_map', {})
    headers = {'Content-Type': 'text/plain', "charset": "UTF-8"}
    mentioned_list = list()
    for name in names:
        mentioned_list.append(names_map.get(name))
    data = {
        "msgtype": "text",
        "text": {
            "content": "上一个工作日【%s】, 还没填写工时的同学请注意填写工时!!" % date,
            "mentioned_list": mentioned_list
        }
    }
    try:
        response = requests.post(webhook, data=json.dumps(data, ensure_ascii=False).encode(encoding='utf-8'), headers=headers)
        logger.debug(response)
    except Exception as e :
        logger.error(e)



if __name__ == '__main__':
    push_message(['林进庭','闵和矗', '马景松', '易尊忠', '邱志基'], '2021-03-04')