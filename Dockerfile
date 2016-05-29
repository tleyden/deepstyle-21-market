
# Note: this doesn't work under docker!
# To start now or restart the service if it's already running:
#  sudo service zerotier-one restart
# sudo systemctl restart zerotier-one.service
# Failed to get D-Bus connection: Unknown error -1

FROM python:3.5-slim

RUN apt-get update -y && \
    apt-get install -y \
    curl \
    gcc \
    musl-dev \
    sudo
                       
RUN pip3 install --upgrade pip
RUN pip3 install two1 
RUN pip3 install flask
RUN 21 update

COPY *.py /root/  