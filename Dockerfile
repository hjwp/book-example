FROM python:3.13-slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<6"

COPY src /src

WORKDIR /src

CMD python manage.py runserver
