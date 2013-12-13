#!/usr/bin/env python
import sys
import pika
import time

#message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(0,100):
    #time.sleep(1)
    message = '%d-burek-...' % i
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print " [x] Sent '%s'" % (message,)


connection.close()
