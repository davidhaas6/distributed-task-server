import os
from celery import Celery

BROKER_URI = "pyamqp://guest@rabbit//"
# BACKEND_URI = os.environ['BACKEND_URI']

app = Celery(
    'celery_app',
    broker=BROKER_URI,
    include=['celery_task_app.tasks']
)
