import gevent
from gevent.event import AsyncResult
a = AsyncResult()

def setter():
    print 'setter starting'
    gevent.sleep(3)
    print 'setter sending message'
    a.set('Hello!')

def waiter():
    print 'waiter starting'
    print 'waiter got message:'+a.get()

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])

print 'end'