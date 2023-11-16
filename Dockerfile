FROM python:3.13-slim

COPY src /src

WORKDIR /src

CMD python manage.py runserver
