FROM opensuse/leap:15.2

MAINTAINER Kyr <kyrylo.shatskyy@gmail.com>

ENV KAFKA_VER "2.7.0"
ENV SCALA_VER "2.13"
ENV KAFKA_ZOOKEEPER_CONNECT "localhost:2181"
ENV KAFKA_ADVERTISED_LISTENERERS "PLAINTEXT://localhost:9092"

RUN zypper --non-interactive ref && \
    zypper --non-interactive up && \
    zypper --non-interactive in java-11-openjdk curl tar gzip

# Get your mirror from here https://www.apache.org/dyn/closer.cgi?path=/kafka/2.7.0/kafka_2.13-2.7.0.tgz

RUN curl -O https://ftp.fau.de/apache/kafka/$KAFKA_VER/kafka_$SCALA_VER-$KAFKA_VER.tgz && \
    tar xzf kafka_$SCALA_VER-$KAFKA_VER.tgz

CMD cd kafka_$SCALA_VER-$KAFKA_VER && bin/kafka-server-start.sh config/server.properties --override zookeeper.connect=$KAFKA_ZOOKEEPER_CONNECT --override advertised.listeners=$KAFKA_ADVERTISED_LISTENERERS


