import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8000')}"
worker_class = "asyncio"
h2_enabled = True
error_logfile = "-"
loglevel = "DEBUG"