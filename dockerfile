FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=./venv/
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Configure app
# ENV BROKER_URI="pyamqp://guest@rabbit//"
# ENV BACKEND_URI="rpc://"
# ENV BROKER_URI="pyamqp://guest:34.122.90.93@rabbit:5672//"
ENV BROKER_URI="pyamqp://guest:**@34.122.90.93:5672//"
ENV BACKEND_URI=""
# ENV MODEL_PATH=""

# Run the application:
COPY app/ ./
COPY task_queue ./task_queue/
CMD ["python3", "main.py"]