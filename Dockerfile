FROM python:3.10-alpine

# Setting PYTHONUNBUFFERED to a non empty value ensures that the python output 
# is sent straight to terminal (e.g. your container log) without being first 
# buffered and that you can see the output of your application (e.g. django logs) 
# in real time. This also ensures that no partial output is held in a buffer 
# somewhere and never written in case the python application crashes.
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
RUN mkdir /app/test

WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user