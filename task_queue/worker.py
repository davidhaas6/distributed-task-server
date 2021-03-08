import os
from celery import Celery

BROKER_URI = os.environ['BROKER_URI']
BACKEND_URI = os.environ['BACKEND_URI']

# Starts the celery instance
app = Celery(
    'celery_app',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['task_queue.tasks']
)
