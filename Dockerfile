FROM python:slim

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install "django<5"

COPY src /src

WORKDIR /src

CMD python manage.py runserver 8888
