#!/usr/bin/env python
import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

for topic in sys.argv[1:]:  #cron.*  *.error ...
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=topic)

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    delivery_tag = method.delivery_tag
    print " [x] Received %r - %s" % (body,delivery_tag)
    
    sleeptime = 2
    time.sleep(sleeptime)

    #ch.basic_ack(delivery_tag=delivery_tag)
    print " [x] Done"


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True) #default

channel.start_consuming()
