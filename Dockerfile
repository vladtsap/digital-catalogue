FROM python:3.9.5-slim

WORKDIR /app

COPY . /app

RUN chmod a+x docker-entrypoint.sh && \
    python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
