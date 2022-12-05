import pika


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

queue = channel.queue_declare(queue='orders')

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

def callback(ch, method, properties, body):
    print(f"secondconsumer - received new message: {body}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue=queue.method.queue, 
    auto_ack=False,
    on_message_callback=callback
)

print("Batata servicve consuming")

channel.start_consuming()