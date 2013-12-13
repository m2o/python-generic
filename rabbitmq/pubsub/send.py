#!/usr/bin/env python
import sys
import pika
import time

#message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')  #broadcasts to all queues bound to the exchange

for i in range(0,100):
    message = '%d-burek-...' % i
    channel.basic_publish(exchange='logs',
                          routing_key='',  #fanout exchanges ignore routing_key values
                          body=message)
    print " [x] Sent '%s'" % (message,)
    time.sleep(1)



connection.close()
