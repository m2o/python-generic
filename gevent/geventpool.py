#from multiprocessing.pool import Pool
from gevent.pool import Pool

import gevent.monkey
gevent.monkey.patch_time()

import gevent
import random
import urllib2
import json
import time

def task(pid):
    #print('Starting task %d' % (pid,))
    time.sleep(random.randint(0,2))
    #print('Finished task %d' % (pid,))
    return pid**2

p = Pool(size=2)

#result = p.apply(task, [1])

#async_result = p.apply_async(task,[1])
#print async_result.ready()
#result = async_result.get()
#print result

#mapresult = p.map(task,xrange(0,10))
#print mapresult

#async_mapresult = p.map_async(task,xrange(0,10))
#print async_mapresult.ready()
#result = async_mapresult.get()
#print result

#imapresult = p.imap(task,xrange(0,10))
#for result in imapresult:
#    print result

imapresult_unordered = p.imap_unordered(task,xrange(0,500))
for result in imapresult_unordered:
    print result