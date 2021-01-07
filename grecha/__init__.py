import sys
import docopt

__doc__ = """
Usage: grecha --help
       grecha watch [options]
       grecha store [options]

Monitor site availability and report to kafka server, safe site availability to database.

Common arguments:
    -K <kafka>, --kafka <kafka>             Kafka brocker host [default: localhost:9092]
    -T <topic>, --topic <topic>             Kafka message topic [default: grecha]
    --kafka-ssl                             Use SSL protocol, instead of PLAINTEXT
    --kafka-ssl-ca <path>                   Kafka ca.pem file path
    --kafka-ssl-cert <path>                 Kafka service.cert path
    --kafka-ssl-key <path>                  Kafka service.key path

Watch specific arguments:
    -w, --wait <seconds>                    Seconds to wait between site checks [default: 5]

Store specific arguments:
    -d, --postgresql-uri <uri>              PostgreSQL database uri, if used then other
                                            connection related options will be ignored
    -H, --postgresql-host <addr>            PostgreSQL host name [default: localhost]
    -P, --postgresql-port <port>            PostgreSQL port number [default: 5432]
    -D, --postgresql-database <database>    PostgreSQL database [default: grecha]
    -U, --postgresql-username <user>        PostgreSQL username [default: grecha]
    -W, --postgresql-password <data>        PostgreSQL password
"""


def main():
    args = docopt.docopt(__doc__, argv=sys.argv[1:])
    print('Hello, this is Kafka Grefneva, enjoy your meal.')
    if args.get('watch'):
        from .watcher import watch
        watch(args)

    elif args.get('store'):
        from .storer import store
        store(args)
        print('Storing database')


