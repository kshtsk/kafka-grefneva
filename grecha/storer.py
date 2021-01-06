import json
import psycopg2
from kafka import KafkaConsumer

def store(args):
    topic = args.get('--topic')
    kafka = args.get('--kafka')
    cafile = args.get('--kafka-ssl-ca')
    certfile = args.get('--kafka-ssl-cert')
    keyfile = args.get('--kafka-ssl-key')
    uri = args.get('--postgresql-uri')
    host = args.get('--postgresql-host')
    port = args.get('--postgresql-port')
    database = args.get('--postgresql-database')
    username = args.get('--postgresql-username')
    password = args.get('--postgresql-password')

    if args.get('--kafka-ssl'):
        k = KafkaConsumer(
            topic,
            bootstrap_servers=kafka,
            security_protocol='SSL',
            ssl_cafile=cafile,
            ssl_certfile=certfile,
            ssl_keyfile=keyfile,
        )
    else:
        k = KafkaConsumer(
            topic,
            bootstrap_servers=kafka,
        )
    if uri:
        postgre = psycopg2.connect(uri)
    else:
        postgre = psycopg2.connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database,
        )
    c = postgre.cursor()
    c.execute(
        "create table if not exists grecha ("
        "url VARCHAR (512) NOT NULL, "
        "date TIMESTAMP NOT NULL, "
        "match VARCHAR, "
        "regex VARCHAR, "
        "status VARCHAR)"
    )
    c.execute(
        "create table if not exists grecha_regex ("
        "id INT not null, "
        "regex VARCHAR, "
        "primary key (id))"
    )
    postgre.commit()
    try:
        for message in k:
            m = json.loads(message.value)
            print(f'got {message.value}')
            regex = m.get('regex', None)
            if regex:
                c.execute('insert into grecha_regex (regex) values (%s)', (regex))
            c.execute(
                "insert into grecha (url, date, status, regex, match) "
                "values (%s, %s, %s, %s, %s)", (
                    m['url'], m['date'], m['status'],
                    m.get('regex'), m.get('match'))
                )
            postgre.commit()
    finally:
        postgre.commit()
    c.close()
    postgre.close()
