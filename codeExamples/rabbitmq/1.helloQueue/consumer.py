import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='helloWorldQueuw')

def callback(ch, method, properties, body):
    print(f"received new message: {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f"Finish Consuming")

channel.basic_consume(
    queue='helloWorldQueuw', 
    auto_ack=False,
    on_message_callback=callback
)

if __name__ == "__main__":
    print("Starting Consuming")
    channel.start_consuming()
    connection.close()