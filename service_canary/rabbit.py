import sys
import socket
try:
    import pika
except ImportError:
    print("RabbitMQ test requested, but pika not installed. "
          "Try 'pip install pika' and try again.")
    sys.exit(1)

def rabbit_check(config):
    host = config.get("host", "localhost")
    port = int(config.get("port", 5672))
    params = pika.ConnectionParameters(host, port)
    try:
        conn = pika.BlockingConnection(params)
        conn.channel()
    except:
        return False
    else:
        return True

