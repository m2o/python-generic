class Worker(object):

	def doA(self):
		print 'A'
	
	def doB(self):
		print 'B'
	
	def doC(self):
		print 'C'
	
	
class Wrapper(object):

	def __init__(self,worker):
		self.worker = worker
		
	def do(self):
		self.worker.doA()
		self.worker.doB()
		self.worker.doC()
		
	def __getattr__(self,attr):
		return getattr(self.worker,attr)
	
w1 = Worker()
w2 = Wrapper(w1)

w2.doA()

w2.do()

