FROM ubuntu:18.04

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get install -qy python3 python3-pip python3-setuptools

RUN pip3 install --quiet xmltodict requests rauth

ADD . /goodreads
WORKDIR /goodreads
