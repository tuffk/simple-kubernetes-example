# set the base image
FROM python:3.7.2

# create directory for the app inside the docker
RUN mkdir -p /app
# move the working context to that directory
WORKDIR /app

# add dependencies file to the docker
COPY requirements.txt /app/requirements.txt
# install the dependencies
RUN pip install -r requirements.txt

# add source files to the docker
COPY server.py server.py
