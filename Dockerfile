FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt
