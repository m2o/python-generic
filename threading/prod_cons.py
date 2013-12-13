import threading
import time

class Producer(threading.Thread):

    def __init__(self,pipe,condition):
        self.pipe = pipe
        self.condition = condition
        super(Producer,self).__init__()
        
    def run(self):
        ints = range(0,10)
        for i in ints:
            with self.condition:
                print 'producer - produced %d' % i
                self.pipe.append(i)
                self.condition.notify()

class Consumer(threading.Thread):

    def __init__(self,pipe,condition):
        self.pipe = pipe
        self.condition = condition
        super(Consumer,self).__init__()
        
    def run(self):
        while True:
            with self.condition:
                while True:
                    if self.pipe:
                        i = self.pipe.pop()
                        print 'consumer - consumed %d' % i
                        break
                    else:
                        self.condition.wait()
                
c = threading.Condition()
f=[]
        
p = Producer(f,c)
c = Consumer(f,c)

p.start()
c.start()

p.join()
c.join()
print 'ending'