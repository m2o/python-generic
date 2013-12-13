#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    delivery_tag = method.delivery_tag
    print " [x] Received %r - %s" % (body,delivery_tag)
    
    value = int(body.split("-")[0])
    sleeptime = 5 if value % 2 == 0 else 0
    time.sleep(sleeptime)

    #ch.basic_ack(delivery_tag=delivery_tag)
    print " [x] Done"


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True) #default

channel.start_consuming()
