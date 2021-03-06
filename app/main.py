# The main entrypoint for the API

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from celery import Celery
from data_models import ModelInput, Task, Prediction
import os

from celery import Celery

BROKER_URI = os.environ['BROKER_URI']
BACKEND_URI = os.environ['BACKEND_URI']

# Create the FastAPI app
app = FastAPI()

# Create celery instance
celery_app = Celery(
    'celery_client',
    broker=BROKER_URI,
    backend=BACKEND_URI,
)
print("celery initialized:", celery_app)


@app.post('/model/predict', response_model=Task, status_code=202)
async def model_predict(data: ModelInput):
    """Create celery prediction task. Return task_id to client in order to retrieve result"""
    task_name='task_queue.tasks.PredictionTask'
    print("sending task")
    task_id = celery_app.send_task(task_name,args=[dict(data)],kwargs={})
    print("sent")
    return {'task_id': str(task_id), 'status': 'Processing'}


@app.get('/model/result/{task_id}',  status_code=200, response_model=Prediction,
         responses={202: {'model': Task, 'description': 'Accepted: Not Ready'}})
async def model_result(task_id):
    """Fetch result for given task_id"""
    task = AsyncResult(task_id)  # Check progrses of task with backend (RabbitMQ in our case)
    if not task.ready():
        print(app.url_path_for('model_predict'))
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    
    # Task is ready, return result
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'probability': str(result)}


