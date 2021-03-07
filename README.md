# FastAPI and Celery Distributed Task Queue
Working example of a distributed task queue using FastAPI and Celery, with a RabbitMQ broker.

## Usage

### Build API and Task Server images

> docker build -t celery_simple:latest .

### Run API, Broker, and Task Server

> docker-compose up