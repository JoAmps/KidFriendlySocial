#!/bin/bash

docker login
docker build --tag joamps/app:latest . -f Dockerfile
docker push joamps/app:latest
