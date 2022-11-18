# syntax=docker/dockerfile:1.3
# changung syntax to enable pip cahing

# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR .

RUN apk update && apk add \
    gcc\
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev cargo \
    cargo \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    gettext

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

