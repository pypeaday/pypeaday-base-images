FROM python:3.10

RUN python3 -m pip install pip --upgrade && python3 -m pip install hatch

COPY . /app

WORKDIR /app

RUN hatch shell

ENTRYPOINT hatch run main
