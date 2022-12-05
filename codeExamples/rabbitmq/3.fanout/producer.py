import pika
from pika.exchange_type import ExchangeType
import sys


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = b" ".join(
    arg.encode() for arg in sys.argv[1:]
) or b"Hello world"

channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()