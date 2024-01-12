#! /bin/sh

TOP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"

GUNICORN=/usr/bin/gunicorn
GUNICORN_CONF=${TOP_DIR}/gunicorn.conf.py
APP=orwebsite.wsgi:application

exec $GUNICORN -c $GUNICORN_CONF $APP

