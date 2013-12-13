import threading
import time

class Producer(threading.Thread):

    def __init__(self,pipe,event):
        self.pipe = pipe
        self.event = event
        super(Producer,self).__init__()
        
    def run(self):
        ints = range(0,10)
        for i in ints:
            time.sleep(1)
            print 'producer - produced %d' % i
            self.pipe.append(i)
            self.event.set()
            self.event.clear()

class Consumer(threading.Thread):

    def __init__(self,pipe,event):
        self.pipe = pipe
        self.event = event
        super(Consumer,self).__init__()
        
    def run(self):
        while True:
            self.event.wait()
            if self.pipe:
                i = self.pipe.pop()
                print 'consumer - consumed %d' % i
                
e = threading.Event()
f=[]
        
p = Producer(f,e)
c = Consumer(f,e)

p.start()
c.start()

p.join()
c.join()
print 'ending'