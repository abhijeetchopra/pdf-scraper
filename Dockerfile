FROM python:latest

# update and upgrade
RUN apt -y update && apt -y upgrade

# install curl
RUN apt install -y curl

# install pip using curl
RUN curl https://bootstrap.pypa.io/get-pip.py | python3

# upgrade pip
RUN python3 -m pip install --upgrade pip

# install dependencies using pip
RUN python3 -m pip install pandas matplotlib pdfquery

# copy scripts
ADD scripts /scripts

# set working directory
WORKDIR /scripts
