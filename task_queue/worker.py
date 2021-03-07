import os
from celery import Celery

BROKER_URI = "pyamqp://guest@rabbit//"
BACKEND_URI = "rpc:// " # RabbitMQ backend

app = Celery(
    'celery_app',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['task_queue.tasks']
)
