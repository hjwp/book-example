FROM python:slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<5" gunicorn whitenoise

COPY src /src

WORKDIR /src

CMD gunicorn --bind :8888 superlists.wsgi:application
