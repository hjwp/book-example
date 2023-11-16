FROM python:3.14-slim

COPY src /src

WORKDIR /src

CMD ["python", "manage.py", "runserver"]
