### gunicorn conf for OrWebSite
import os

TOP_DIR = os.path.abspath(os.path.dirname(__file__))

## App path
chdir = TOP_DIR

## Python path
pythonpath = '/usr/bin/python3'

## Server Socket
bind = '192.168.56.101:55181'

backlog = 2048

## reload app when app update
reload = False

## Worker Processes
workers = 2
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000
timeout = 30
keepalive = 2

debug = False
spew = False

## Server Mechanics
preload_app = True
daemon = True
pidfile = chdir + '/gunicorn.pid'

## Logging
accesslog = chdir + '/gunicorn_access.log'
errorlog = chdir + '/gunicorn_error.log'
loglevel = 'debug'
#logconfig = chdir + '/gunicorn.log'

## Process Naming
proc_name = 'orwebsite'
