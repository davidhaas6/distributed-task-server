
from fastapi import FastAPI
from pydantic import BaseModel

from tasks import add

# Create the FastAPI app
app = FastAPI()


# Use pydantic to keep track of the input request payload
class Numbers(BaseModel):
    x: float
    y: float


@app.post('/add')
def enqueue_add(n: Numbers):
    # We use celery delay method in order to enqueue the task with the given parameters
    add.delay(n.x, n.y)