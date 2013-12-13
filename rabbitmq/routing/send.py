#!/usr/bin/env python
import sys
import pika
import time

SEVERITIES = ['debug','info','error']

#message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

for i in range(0,100):
    
    severity = SEVERITIES[i%3]
    
    message = '%s - %d - burek - ...' % (severity,i)
    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=message)
    print " [x] Sent '%s'" % (message,)
    time.sleep(1)

connection.close()
