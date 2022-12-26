FROM alpine

ARG BASE_VERSION

ENV BASE_VERSION=$BASE_VERSION

RUN apk update && apk upgrade && rm -rf /var/cache/apk/*

WORKDIR /app

COPY ./hello.sh hello.sh

ENTRYPOINT ["./hello.sh"]
