import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type=ExchangeType.topic)

payments_message = 'User place order'

channel.basic_publish(exchange='orders', routing_key='order-placed', body=payments_message)

print(f'sent message: {payments_message}')
