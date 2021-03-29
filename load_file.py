#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/19 8:57
@Author:  linjinting
@File: load_file.py
@Software: PyCharm
"""

import json
import logging
import io
logger = logging.getLogger("worker.load")

_JSON_DATA = {
  "custom_worker_day": [],
  "custom_rest_day": [],
  "extra_names": [],
  "client": {
    "api_reqworktime": "http://10.7.3.32:9002/reqworktimelong",
    "api_webhook" : "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=75296043-f005-45ea-8a9b-c4b07b87aba5",
    "api_holiday": "http://xxxxxxxxxxx/"
  },
"names_map" : { "林进庭":"linjinting", "闵和矗":"minhechu", "邱志基":"qiuzhiji", "马景松":"majingsong", "易尊忠":"yizunzhong"}
}

def load_json():
    try:
        with io.open("custom_date.json", encoding='utf-8') as fp:
            json_data = json.load(fp)
    except Exception as e:
        logger.error(e)
        json_data = _JSON_DATA

    return json_data

JSON_DATA = load_json()

if __name__ == '__main__':
    print(JSON_DATA)