
from fastapi import FastAPI
from pydantic import BaseModel
from celery_task_app.tasks import predict_churn_single



# Create the FastAPI app
app = FastAPI()
predict_churn_single.delay({1:9})

# Use pydantic to keep track of the input request payload
class Numbers(BaseModel):
    x: float
    y: float


@app.post('/churn/predict', status_code=202)
async def churn():
    """Create celery prediction task. Return task_id to client in order to retrieve result"""
    task_id = predict_churn_single.delay(['good','data'])
    print(task_id)
    return {'task_id': str(task_id), 'status': 'Processing'}