FROM python:3.12-alpine AS base

RUN apk --no-cache add git build-base libffi-dev
WORKDIR /app
RUN git clone -b dev https://github.com/Pavel-Igorevich/FastAPI-SQLalchemy-Alembic.git .
RUN pip3 install --upgrade setuptools && pip3 install -r requirements.txt