import pika
import sys


connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='workers')

message = b" ".join(
    arg.encode() for arg in sys.argv[1:]
) or b"Hello world"


if __name__ == "__main__":
    message = f"Sending Message Id: {message}"
    channel.basic_publish(exchange='', routing_key='workers', body=message)
    print(f"sent message: {message}")
