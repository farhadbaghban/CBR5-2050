FROM python

RUN pip install psycopg2-binary

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY ./requirments /requirments
RUN pip install -U pip && pip install -r /requirments/development.txt

COPY ./src /src
WORKDIR /src

EXPOSE 8000