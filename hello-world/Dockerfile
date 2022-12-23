FROM alpine

RUN apk update && apk upgrade && rm -rf /var/cache/apk/*

WORKDIR /app

COPY ./hello.sh hello.sh

ENTRYPOINT ["./hello.sh"]
