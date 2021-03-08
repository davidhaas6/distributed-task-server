# builds and runs the servers
docker build -t task_server:latest .
docker-compose -f client.yml up