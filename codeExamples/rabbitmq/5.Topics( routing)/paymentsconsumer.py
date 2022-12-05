import pika
from pika.exchange_type import ExchangeType
import time

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='orders', queue=queue.method.queue, routing_key='order-placed')

def callback(ch, method, properties, body):
    print(f'Payments - received new message: {body}')

    message = 'order paid'

    time.sleep(4)
    channel.basic_publish(exchange='orders', routing_key='order-paid', body=message)
    print(f'sent message: {message}')


channel.basic_consume(
    queue=queue.method.queue, 
    auto_ack=True,
    on_message_callback=callback
)

print('Payments Starting Consuming')

channel.start_consuming()