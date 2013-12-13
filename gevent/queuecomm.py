import random

import gevent
from gevent.queue import Queue, Empty
from gevent.pool import Group
from gevent import getcurrent
from gevent.local import local

taskqueue = Queue(maxsize=5)
workerdata = local()

def worker(pid):
    print 'worker #%d-%s starting' % (pid,id(getcurrent()))
    workerdata.cnt = 0
    while True:
        try:
            task = taskqueue.get(timeout=5)
            workerdata.cnt += 1
            print 'worker #%d got task #%d' % (pid,task)
            gevent.sleep(random.randint(0,3))
        except Empty:
            break
    print 'worker #%d-%s exiting (cnt:%d)' % (pid,id(getcurrent()),workerdata.cnt)

def boss():
    print 'boss starting'
    for i in xrange(0,15):
        taskqueue.put(i)
    print 'boss completed'


g = Group()
g.add(gevent.spawn(boss))
map(g.add,(gevent.spawn(worker,i) for i in xrange(0,3)))

print 'all spawned'
gevent.joinall(g)
print 'end'