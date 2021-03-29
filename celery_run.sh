#!/bin/bash

case $1 in
   start)  celery multi start worker -A  celery_app -l info -B --logfile=celerylog.log;;
   stop) celery multi stop worker -A  celery_app -l info -B --logfile=celerylog.log;;
   restart) celery multi restart worker -A  celery_app -l info -B --logfile=celerylog.log;;
   *) echo "require start|stop" ;;
esac

tail -f celerylog.log