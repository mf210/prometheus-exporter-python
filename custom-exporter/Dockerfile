FROM python:3.12
WORKDIR /prometheus-exporter
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /prometheus-exporter/
RUN pip install pipenv && pipenv install --dev --system