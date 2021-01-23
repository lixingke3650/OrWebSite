#! /bin/sh

GUNICORN=/usr/bin/gunicorn
GUNICORN_CONF=/home/hanbin/web/orwebsite/gunicorn.conf.py
APP=orwebsite.wsgi:application

exec $GUNICORN -c $GUNICORN_CONF $APP

