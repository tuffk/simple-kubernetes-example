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

# gunicorn starts the server
ENTRYPOINT ["gunicorn", "-w", "1", "--chdir", "/app", "server:app", "-b", ":8000", "--name=app", "--access-logfile=-"]

# run locally
# building
# docker build -t catedra .
# runnning
# docker run --rm --name potatoes -e HELLO_ENV=dokcer -p 8000:8000 catedra
