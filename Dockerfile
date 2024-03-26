FROM python:3.13-slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src /src

WORKDIR /src

CMD gunicorn --bind :8888 superlists.wsgi:application
