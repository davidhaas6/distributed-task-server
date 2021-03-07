
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult

from models import ModelInput, Task, Prediction
from task_queue.tasks import predict_objective


# Create the FastAPI app
app = FastAPI()


@app.post('/model/predict', response_model=Task, status_code=202)
async def model_predict(data: ModelInput):
    """Create celery prediction task. Return task_id to client in order to retrieve result"""
    task_id = predict_objective.delay(dict(data))
    # print(task_id)
    return {'task_id': str(task_id), 'status': 'Processing'}


@app.get('/model/result/{task_id}',  status_code=200, response_model=Prediction,
         responses={202: {'model': Task, 'description': 'Accepted: Not Ready'}})
async def model_result(task_id):
    """Fetch result for given task_id"""
    task = AsyncResult(task_id)
    if not task.ready():
        print(app.url_path_for('model_predict'))
        return JSONResponse(status_code=202, content={'task_id': str(task_id), 'status': 'Processing'})
    result = task.get()
    return {'task_id': task_id, 'status': 'Success', 'probability': str(result)}


