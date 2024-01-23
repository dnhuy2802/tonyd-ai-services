FROM python:3.10-slim-bookworm
LABEL version="1.0"
LABEL description="TonyD Service"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN apt update && apt install -y ffmpeg

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

# RUN pip install -r /code/requirements.txt

# COPY . /code

CMD python main.py