FROM python:3.7-slim

RUN apt -y update && apt -y upgrade
RUN apt install -y curl

RUN curl https://bootstrap.pypa.io/get-pip.py | python3

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install pandas matplotlib pdfquery

ADD scripts /scripts

WORKDIR /scripts
