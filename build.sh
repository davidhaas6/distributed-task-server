# builds and runs the servers
docker build -f local-dockerfile -t task_server:latest .
docker-compose up