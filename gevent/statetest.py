import gevent

import random
import urllib2
import json

def ok(name):
    print('Starting task %s' % (name,))
    gevent.sleep(random.randint(0,1))
    print('Finished task %s' % (name,))
    return 'ok!'

def notok(name):
    print('Starting task %s' % (name,))
    gevent.sleep(random.randint(0,1))
    raise ValueError(name)


t1 = gevent.spawn(ok,'t1')
t2 = gevent.spawn(notok,'t2')

print(t1.started) # True
print(t2.started)  # True

gevent.joinall((t1,t2))

print(t1.value) # 'You win!'
print(t2.value)  # None

print(t1.ready()) # True
print(t2.ready())  # True

print(t1.successful()) # True
print(t2.successful())  # False

# The exception raised in fail, will not propogate outside the
# greenlet. A stack trace will be printed to stdout but it
# will not unwind the stack of the parent.

print(t1.exception)
print(t2.exception)

print t1.get()
try:
    print t2.get()
except ValueError:
    print 'valueerror in t2'