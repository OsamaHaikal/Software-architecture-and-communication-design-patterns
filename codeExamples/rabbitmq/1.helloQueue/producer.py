import pika
import sys

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='helloWorldQueuw')
channel.basic_qos(prefetch_count=1)

default = "Hello this is my first message"
message = b" ".join(
    arg.encode() for arg in sys.argv[1:]
) or default


if __name__ == "__main__":

    channel.basic_publish(exchange='', routing_key='helloWorldQueuw', body=message)

    print(f"sent message: {message}")

    connection.close()