FROM python:3.10-slim-bookworm
LABEL version="1.0"
LABEL description="TonyD Service"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code

CMD python main.py