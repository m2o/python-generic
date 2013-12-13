import socket
print socket.socket
print 'before monkeypatch:',socket.socket

import gevent.monkey
gevent.monkey.patch_socket()

print 'after monkeypatch:',socket.socket

import gevent
import random
import urllib2
import json

def task(pid):
    print('Starting task %d' % (pid,))
    gevent.sleep(random.randint(0,5))
    print('Finished task %d' % (pid,))

def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print 'Process ', pid, datetime
    return json_result['datetime']

def sync():
    for i in range(0,10):
        fetch(i)

def async():
    tasks = [gevent.spawn(fetch,id) for id in xrange(0,10)]
    gevent.joinall(tasks)

#sync()
async()

#print 'after joinall'