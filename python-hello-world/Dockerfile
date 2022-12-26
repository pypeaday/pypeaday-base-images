FROM python:3.10-slim

ARG BASE_VERSION

ENV BASE_VERSION=$BASE_VERSION

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    # apt-get install --no-install-recommends --assume-yes \
    # package-a \
    rm -r /var/lib/apt/lists/*

# TODO: create a virtual environment that any of my python projects can build off of called "my-env" or something
RUN python3 -m pip install pip --upgrade --no-cache-dir && python3 -m pip install hatch --no-cache-dir

COPY . /app

WORKDIR /app

RUN hatch env create

ENTRYPOINT ["hatch", "run", "main"]
