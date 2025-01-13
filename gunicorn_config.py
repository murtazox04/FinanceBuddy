import multiprocessing

# Server socket settings
bind = "0.0.0.0:8004"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 300
keepalive = 2

# Process naming
proc_name = "finance_buddy"

# Logging
errorlog = "/var/log/gunicorn/error.log"
accesslog = "/var/log/gunicorn/access.log"
loglevel = "info"

# Reload
reload = True

# SSL (if needed)
# keyfile = ""
# certfile = ""
