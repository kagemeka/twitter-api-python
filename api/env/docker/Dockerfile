FROM ubuntu:20.04 as dev

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noniteractive

RUN \
  apt update -q=2 \
  && apt install -y \
  python3-pip \
  wget \
  curl

COPY py/requirements.txt .
RUN \
  pip install -r requirements.txt \
  && rm requirements.txt