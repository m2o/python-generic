#!/usr/bin/env python
import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare('rpc_queue')

print ' [*] Waiting for messages. To exit press CTRL+C'

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def callback(ch, method, props, body):
    delivery_tag = method.delivery_tag
    correlation_id = props.correlation_id
    reply_to = props.reply_to
    
    n = int(body)
    print " [x] Received %s - %s - %s -%s" % (body,delivery_tag,correlation_id,reply_to)
    
    response = fib(n)
    
    ch.basic_publish(exchange='',
                     routing_key=reply_to,
                     properties=pika.BasicProperties(correlation_id = correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

    print " [x] Done"


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='rpc_queue',
                      no_ack=False) #default

channel.start_consuming()
