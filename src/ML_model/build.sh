#!/bin/bash

docker login
docker build --tag joamps/ml-model:latest . -f Dockerfile
docker push joamps/ml-model:latest
