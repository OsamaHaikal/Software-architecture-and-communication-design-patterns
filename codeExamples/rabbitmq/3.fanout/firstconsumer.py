import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue = channel.queue_declare(queue='emails', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

def callback(ch, method, properties, body):
    print(f"firstconsumer - received new message: {body}")

channel.basic_consume(
    queue=queue.method.queue, 
    auto_ack=False,
    on_message_callback=callback
)

print("Email service consuming")

channel.start_consuming()