FROM ubuntu:16.04

RUN apt-get update -qq \
  && apt-get install -y \
  zip \
  python2.7 \
  python-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN python2 -m pip install --upgrade pip \
    && python2 -m pip install boto3

RUN mkdir /engine
WORKDIR /engine
COPY ./app /engine
