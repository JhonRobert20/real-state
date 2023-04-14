FROM python:3.11-bullseye AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /home/ubuntu/webs/real_state/real_state
RUN set -ex; apt-get update ; apt install -y --no-install-recommends gcc python3-dev build-essential ; pip install --upgrade pip --no-cache ;

COPY pyproject.toml /home/ubuntu/webs/real_state/real_state
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY . .

FROM builder AS local
RUN poetry install
