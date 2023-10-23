# syntax=docker/dockerfile:1

FROM python:3.10.13-slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /python-docker


ENTRYPOINT [ "python" ]

CMD ["app.py" ]