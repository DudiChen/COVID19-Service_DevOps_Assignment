FROM python:3.8-alpine

WORKDIR /covid_service

COPY ./requirements.txt /tmp

RUN apk add curl && \
	pip3 install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8080

COPY . /covid_service

ENV FLASK_APP /covid_service/app/app.py

CMD ["flask","run", "--port=8080", "--host=0.0.0.0"]
