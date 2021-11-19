FROM arm32v7/python:3.9-buster

ENV CFLAGS=-fcommon
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libatlas-base-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV LD_LIBRARY_PATH /opt/vc/lib

