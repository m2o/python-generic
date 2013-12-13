def grep(pattern,lines):
    for line in lines:
        if pattern in line:
            yield line


def grep1(pattern):
    while True:
        line = (yield)
        if pattern in line:
            print line

a = ['abc','baba','caca']

a = (v for v in a)
a = grep('b',a)

print list(a)


b = grep1("ruby")
print b.next() #priming

b.send("helloworld!")
b.send("hello ruby!")
b.send("burek!")

from coroutine import coroutine

@coroutine
def grep3(pattern):
    try:
        while True:
            line = (yield)
            if pattern in line:
                print line
    except ValueError,v:
        print 'value error!',v
    except GeneratorExit:
        print 'bye!'

b = grep3("ub")
b.send("helloworld!")
b.send("hello ruby!")
b.send("bubrek!")
#b.throw(ValueError,'error burek!')
b.close()

import time

@coroutine
def follow(fobj,targets):
    f.seek(0,2)
    while True:
        line = f.readline()
        if line:
            for t in targets:
                t.send(line.strip())
        else:
            time.sleep(0.1)
@coroutine
def grep4(pattern,printer):
    try:
        while True:
            line = (yield)
            if pattern in line:
                printer.send('>%s<-%s' % (pattern,line))
    except ValueError,v:
        print 'value error!',v
    except GeneratorExit:
        print 'bye!'



@coroutine
def printer():
    while True:
        line = (yield)
        print line

print 'start'
f = open('dummy.log','r')
p = printer()
targets = [grep4('',p),grep4('a',p),grep4('python',p)]
follow(f,targets)

