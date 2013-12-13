import threading
import time

class Worker(threading.Thread):

    def __init__(self,fd,lock):
        self.fd = fd
        self.lock = lock
        super(Worker,self).__init__()
        
    def run(self):
        for i in range(1,10):
            time.sleep(1)
            with self.lock:
                #self.lock.acquire()
                self.fd.write(('%s '%self.ident) * i + '\n')
                #self.lock.release()      
        
f = open('result.txt','w')

l = threading.Lock()
        
w1 = Worker(f,l)
w2 = Worker(f,l)

w1.start()
w2.start()

w1.join()
w2.join()
f.close()
print 'ending'