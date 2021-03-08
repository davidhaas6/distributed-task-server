#!/bin/bash
# builds and runs the servers

if [[ $1 == "client" ]]; then
echo "Building API environment"
    docker build -f client-dockerfile -t api_client:latest .
    docker-compose -f client-compose.yml up
elif [[ $1 == "server" ]]; then
    echo "Building Task Server environment"
    docker build -f taskserver-dockerfile -t task_server:latest .
    docker-compose -f taskserver-compose.yml up
else
    echo "Building Local Dev Environment"
    docker build -f taskserver-dockerfile -t task_server:latest .
    docker build -f client-dockerfile -t api_client:latest .
    docker-compose -f docker-compose.yml up
fi
