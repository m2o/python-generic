import signal
import random
import urllib2
import json

import gevent
from gevent import Timeout

def task(pid):
    print('Starting task %d' % (pid,))
    gevent.sleep(100)
    print('Finished task %d' % (pid,))

def async():
    timer = Timeout(2).start()
    tasks = [gevent.spawn(task,id) for id in xrange(0,10)]
    try:
        gevent.joinall(tasks,timeout = timer)
    except Timeout:
        print 'timeout!!!'
#sync()

async()
print 'after joinall'