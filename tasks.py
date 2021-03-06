from celery import Celery
from celery.utils.log import get_task_logger

# Create the celery app and get the logger
celery_app = Celery('tasks', broker='pyamqp://guest@rabbit//')
logger = get_task_logger(__name__)


@celery_app.task
def add(x, y):
    res = x + y
    logger.info("Adding %s + %s, res: %s" % (x, y, res))
    return res