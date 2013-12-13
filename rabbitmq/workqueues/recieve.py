#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    delivery_tag = method.delivery_tag
    print " [x] Received %r - %s" % (body,delivery_tag)
    
    value = int(body.split("-")[0])
    
    if value % 2 == 0:
        #sleeptime = 1
        #time.sleep(sleeptime)
        ch.basic_ack(delivery_tag=delivery_tag)
        print " [x] Done"
    else:
        ch.basic_reject(delivery_tag=delivery_tag,requeue=False)
        print " [x] rejected"

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

channel.start_consuming()
