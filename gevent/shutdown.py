import gevent
import signal
import random
import urllib2
import json

def task(pid):
    print('Starting task %d' % (pid,))
    gevent.sleep(100)
    print('Finished task %d' % (pid,))

def async():
    tasks = [gevent.spawn(task,id) for id in xrange(0,10)]
    gevent.joinall(tasks)

#sync()

gevent.signal(signal.SIGQUIT, gevent.shutdown)

async()
print 'after joinall'