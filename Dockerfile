FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt