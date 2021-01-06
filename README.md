# Introduction

This is another one example project for kafka producer/consumer written in python.


## Installation


```bash
virtualenv -p python3 v
. v/bin/activate
```

For development purpose it can be installed very easily from the source code.

```bash
git clone https://github.com/.../kafka-grefneva
cd kafka-grefneva && pip install .
```

Or use `python` exclusively within your virtual environment:

```bash
python setup install
```

Also you can use:

```bash
pip install git+https://github.com/.../kafka-grefneva@tag

```


## Local Test Environment

### Start Kafka Brocker

Using any of the following ways to start kafka brocker.

#### Supplimentary Docker Compose Way

Make sure you have docker and docker-compose installed and configured in your system.
This manual does not cover 
Once you're ready run the next command in separate terminal:

```bash
docker-compose up
```

It should build required images and start zookeeper and kafka brocker containers for you.

#### Apache Kafka Way

Download and run kafka zookeeper and kafka brocker in separate terminals.

For example go to https://kafka.apache.org/downloads or find close mirror to you directly from here:
https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka-2.7.0-src.tgz

The Apache Kafka Quickstart page https://kafka.apache.org/quickstart includes basic instructions
how to start kafka broker.

For this within the kafka binary run zookeeper in one terminal like that:

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

and the brocker in another as follows:

```bash
bin/kafka-server-start.sh config/server.properties
```


### Start PostgreSQL Database

Make sure you have database running, for example, use postgres docker:

```bash
docker run --name grecha-postgres -e POSTGRES_DB=grecha -e POSTGRES_USER=grecha -e POSTGRES_PASSWORD=qw3r56 -e PGDATA=/var/lib/postgresql/data/pgdata -v /tmp/grecha/db:/var/lib/postgresql/data -p 5432:5432 postgres
```

### Start Webservice

Start example webservice on your localhost like that:

```bash
(cd tests/www ; python3 -m http.server 8081)
```

### Run kafka producer

In order to run site checker producer execute following command:

```bash
grecha watch
```

### Run kafka consumer

In order to run site checker consumer execute following command:

```bash
grecha store -W qw3r56
```


### Hints

You can modify and restart.

```bash
pip uninstall -y kafka-grefneva ; pip install  . ; grecha watch
```

Look at the database:

```bash
psql -h localhost -U grecha grecha -c 'select * from grecha;'
```


## Using with Aiven Services

Make sure you've got created a topic via Aiven Console in "Topics" tab of your Kafka service which should be obviousely running.
Presumably you've downloaded ssl ca, ssl cert and ssl key files saved into your home directory:
```bash
.aiven/kafka/ca.pem
.aiven/kafka/service.cert
.aiven/kafka/service.key
```

Start kafka producer:

```bash
grecha watch -K <kafka-service-uri> --kafka-ssl --kafka-ssl-ca ~/.aiven/kafka/ca.pem --kafka-ssl-cert ~/.aiven/kafka/service.cert --kafka-ssl-key ~/.aiven/kafka/service.key -T <topic>
```

Start kafka consumer:

```bash
grecha store -d <postgresql-service-uri> -K <kafka-service-uri> --kafka-ssl --kafka-ssl-ca ~/.aiven/kafka/ca.pem --kafka-ssl-cert ~/.aiven/kafka/service.cert --kafka-ssl-key ~/.aiven/kafka/service.key -T <topic>
```
