FROM python:slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<6"

COPY src /src

WORKDIR /src

RUN python manage.py migrate --noinput
CMD python manage.py runserver 0.0.0.0:8888
