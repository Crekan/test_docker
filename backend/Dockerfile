FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir /test_docker

WORKDIR /test_docker
EXPOSE 8000

COPY requirements.txt /test_docker/
COPY test_docker /test_docker

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY . /test_docker/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
