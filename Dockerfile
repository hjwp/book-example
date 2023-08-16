FROM python:slim

RUN python -m venv /venv

COPY requirements.txt requirements.txt
RUN /venv/bin/python -m pip install -r requirements.txt

COPY src /src

WORKDIR /src
CMD /venv/bin/python ./manage.py runserver --nothreading 0.0.0.0:8888
