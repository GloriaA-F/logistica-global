bind = "127.0.0.1:8000"
workers = 3
worker_class = "sync"
timeout = 120
accesslog = "/var/www/html/logistica/logs/gunicorn_access.log"
errorlog = "/var/www/html/logistica/logs/gunicorn_error.log"
loglevel = "info"
