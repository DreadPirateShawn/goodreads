FROM ubuntu:18.04 AS base-build

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get install -qy python3 python3-pip python3-setuptools

RUN pip3 install --quiet xmltodict requests rauth

###################################################################

FROM base-build AS base-tests

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get -qq update \
    && apt-get install -qy python3-requests-mock

RUN pip3 install --quiet nose nose_timer coverage mock==2.0.0 \
    && pip3 install --quiet pylint==1.2.1 astroid==1.1.1

###################################################################

FROM base-build AS runtime
ADD . /goodreads
WORKDIR /goodreads

###################################################################

FROM base-tests AS testing
ADD . /goodreads
WORKDIR /goodreads
