
FROM alpine:3.13.5

RUN apk update
RUN apk add scapy python3 && ln -sf python3 /usr/bin/python

RUN mkdir /code
WORKDIR /code
ADD advertise.py /code/

CMD ["python", "-u", "/code/advertise.py"]