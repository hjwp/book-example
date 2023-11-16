FROM python:slim

COPY src /src

WORKDIR /src

CMD python manage.py runserver
