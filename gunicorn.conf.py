### gunicorn conf for OrWebSite

## App path
chdir = '/home/hanbin/web/OrWebSite'

## Python path
pythonpath = '/usr/bin/python3'

## Server Socket
bind = '127.0.0.1:5058'

backlog = 2048

## reload app when app update
reload = True

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
loglevel = 'info'
logconfig = None

## Process Naming
proc_name = 'orwebsite'

