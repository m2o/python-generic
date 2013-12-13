import gevent
from gevent import Greenlet

import random
import urllib2
import json

class Task(Greenlet):

    def __init__(self,name):
        super(Task,self).__init__()
        self.name = name

    def _run(self):
        print('Starting task %s' % (self.name,))
        gevent.sleep(random.randint(0,5))
        print('Finished task %s' % (self.name,))


t1 = Task('hello')
t2 = Task('world')

t1.start()
t2.start()

t1.join()
t2.join()

print 'end'