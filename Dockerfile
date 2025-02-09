FROM python:3.12.8-slim AS build

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD python ./src/main.py
