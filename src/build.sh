#!/bin/bash

doctl registry login
docker build --platform=linux/x86_64 -t app:latest . -f Dockerfile
docker tag app:latest registry.digitalocean.com/kidfriendlysocial/app:latest
docker push registry.digitalocean.com/kidfriendlysocial/app:latest
