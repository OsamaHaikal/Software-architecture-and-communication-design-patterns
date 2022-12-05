import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='orders', queue=queue.method.queue, routing_key='order-paid')

def callback(ch, method, properties, body):
    print(f'Analytics - received new message: {body}')

channel.basic_consume(
    queue=queue.method.queue, 
    auto_ack=True,
    on_message_callback=callback
)

print('Analytics Starting Consuming')

channel.start_consuming()