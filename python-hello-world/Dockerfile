FROM python:3.10

RUN python3 -m pip install pip --upgrade --no-cache-dir && python3 -m pip install hatch --no-cache-dir

COPY . /app

WORKDIR /app

RUN hatch shell

ENTRYPOINT ["hatch", "run", "main"]
