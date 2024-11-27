#!/bin/bash
set -ex

docker ps -q --filter ancestor=superlists | xargs -r docker kill
docker build -t superlists . && docker run \
    -p 8888:8888 \
    --mount type=bind,source=./src/db.sqlite3,target=/src/db.sqlite3 \
    -e DJANGO_SECRET_KEY=sekrit \
    -e DJANGO_ALLOWED_HOST=localhost \
    -e EMAIL_PASSWORD \
    -it superlists
