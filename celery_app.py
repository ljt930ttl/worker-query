#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2021/3/23 11:06
@Author:  linjinting
@File: celery_task.py
@Software: PyCharm
"""

from celery import Celery

from celery.schedules import crontab
app = Celery('tasks-worker', broker='redis://:123456@10.7.3.53:6379/10')
app.conf.timezone ='Asia/Shanghai'

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-day-morning': {
        'task': 'run.run',
        'schedule': crontab(hour=8, minute=30),
    },
    'add-every-30-seconds': {
        'task': 'run.test',
        'schedule': 10.0,
    },
}

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(30.0, test.s('world'), expires=10)
#
#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=8, minute=30, day_of_week=1),
#         run.s(),
#     )
