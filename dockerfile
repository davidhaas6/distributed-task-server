FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=./venv/
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY app/ ./
CMD ["python3", "main.py"]