FROM python:3.10-slim

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    # apt-get install --no-install-recommends --assume-yes \
    # package-a \
    rm /var/lib/apt/lists/*


RUN python3 -m pip install pip --upgrade --no-cache-dir && python3 -m pip install hatch --no-cache-dir

COPY . /app

WORKDIR /app

RUN hatch shell

ENTRYPOINT ["hatch", "run", "main"]
