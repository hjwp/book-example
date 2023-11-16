FROM python:3.12-slim

COPY src /src

WORKDIR /src

CMD python manage.py runserver
