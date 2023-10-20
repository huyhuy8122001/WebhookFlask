# syntax=docker/dockerfile:1

FROM python:3.10.13-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./point_change_event.py ./python-docker//point_change_event.py
COPY ./app.py ./python-docker

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]