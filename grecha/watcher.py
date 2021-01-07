"""
Kafka producer module
"""
import json
import time

from kafka import KafkaProducer

from .checkers import BasicChecker
from .checkers.regex import AnyChecker, RegexChecker
from .checkers.example import ExampleChecker


sites = [
    BasicChecker('http://localhost:8081/'),
    BasicChecker('http://localhost:8081/missing'),
    AnyChecker('http://localhost:8081/'),
    ExampleChecker('http://localhost:8081/'),
    ExampleChecker('http://doesnotexists:8081/'),
    RegexChecker('http://localhost:8081/', ['[Hh]ello\s+[Ww]orld'])
    ]

def watch(args):
    """
    Kafka producer method: watch the sites and check the contents

    Connects to kafka broker, goes through the list of sites and does
    the checking and sends a message containing site availability
    to the kafka service.

    Supports following arguments:

    :arg    --topic:            topic name
    :arg    --kafka:            kafka service uri
    :arg    --wait:             number of seconds to wait between check tries
    :arg    --kafka-ssl:        use ssl proto for kafka
    :arg    --kafka-ssl-ca:     kafka ssl ca file path
    :arg    --kafka-ssl-cert:   kafka ssl cert file path
    :arg    --kafka-ssl-key:    kafka ssl key file path

    """
    topic = args.get('--topic')
    kafka = args.get('--kafka')
    pause = int(args.get('--wait'))
    cafile = args.get('--kafka-ssl-ca')
    certfile = args.get('--kafka-ssl-cert')
    keyfile = args.get('--kafka-ssl-key')

    tojson=lambda v: json.dumps(v).encode('utf-8')

    if args.get('--kafka-ssl'):
        p = KafkaProducer(
                bootstrap_servers=kafka,
                value_serializer=tojson,
                security_protocol='SSL',
                ssl_cafile=cafile,
                ssl_certfile=certfile,
                ssl_keyfile=keyfile,
            )

    else:
        p = KafkaProducer(
                bootstrap_servers=kafka,
                value_serializer=tojson,
            )
    print(f'Watching for sites: {sites}')
    while True:
        for i in sites:
            message = i.check()
            print(f'Sending message to topic "{topic}": {message}')
            p.send(topic, message)
        time.sleep(pause)
