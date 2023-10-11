FROM python:3.12-slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<6" gunicorn

COPY src /src

WORKDIR /src

CMD gunicorn --bind :8888 superlists.wsgi:application
