import json
import time

from kafka import KafkaProducer

from .checkers import BasicChecker
from .checkers.regex import AnyChecker, RegexChecker
from .checkers.example import ExampleChecker

def watch(args):
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

    sites = [
        BasicChecker('http://localhost:8081/'),
        BasicChecker('http://localhost:8081/missing'),
        AnyChecker('http://localhost:8081/'),
        ExampleChecker('http://localhost:8081/'),
        ExampleChecker('http://doesnotexists:8081/'),
        RegexChecker('http://localhost:8081/', ['[Hh]ello\s+[Ww]orld'])
        ]
    print(f'Watching for sites: {sites}')
    while True:
        for i in sites:
            message = i.check()
            #message = json.dumps(i.check()).encode()
            print(f'Sending message to topic "{topic}": {message}')
            p.send(topic, message)
        time.sleep(pause)
