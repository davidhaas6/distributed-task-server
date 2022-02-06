# Data models for our API

from pydantic import BaseModel
from typing import List


class ModelInput(BaseModel):
    """ Example Model Input Features """
    features: List[float]

class Task(BaseModel):
    """ Celery task representation """
    task_id: str
    status: str


class Prediction(BaseModel):
    """ Prediction task result """
    task_id: str
    status: str
    probability: float
