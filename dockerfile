FROM python:3.11

RUN mkdir /main_app

WORKDIR /main_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

WORKDIR /fastapi_app

