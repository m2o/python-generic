#!/usr/bin/env python
import sys
import pika
import time

SEVERITIES = ['debug','info','error']
FACILITIES = ['cron','auth']

#message = ' '.join(sys.argv[1:]) or "Hello World!"

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

for i in range(0,10):
    for facility in FACILITIES:
        for severity in SEVERITIES:
    
            facsev = '%s.%s' % (facility,severity)
            
            message = '%s - %d - burek - ...' % (facsev,i)
            channel.basic_publish(exchange='topic_logs',
                                  routing_key=facsev,
                                  body=message)
            print " [x] Sent '%s'" % (message,)
            time.sleep(1)

connection.close()
