FROM python:3.6-alpine

ENV PYTHONBUFFERED 1

RUN apk update

RUN apk add build-base

RUN apk add jpeg-dev

RUN apk add zlib-dev

ENV LIBRARY_PATH=/lib:/usr/lib

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py migrate

EXPOSE 8080

CMD python manage.py runserver 0:$PORT

