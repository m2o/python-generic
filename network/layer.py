import time
from itertools import cycle
from Queue import Empty

class Layer(object):

	def __init__(self,name):
		self.name = name
		
	def __call__(self,upRead,upWrite,downRead,downWrite):		
		while True:
			for (qRead,qWrite) in ((upRead,downWrite),(downRead,upWrite)):
				try:
					p = qRead.get(block=False)
					qWrite.put(p)
					print '%s - passing message' % (self.name,)
				except Empty:
					pass
			time.sleep(0.001)
			
class NetworkLayer(Layer):

	def __init__(self,name,messages):
		self.name = name
		self.outmessages = messages
		self.inmessages = []
		
	def __call__(self,upRead,upWrite,downRead,downWrite):

		map(downWrite.put,self.outmessages)
		
		while True:				
			res = downRead.get()
			self.inmessages.append(res)
			assert len(self.inmessages)<2 or self.inmessages[-2]+1 == self.inmessages[-1], 'not in order!'
			print '%s - recieved: %s' % (self.name,res)
			
class EchoServer(object):

	def __init__(self):
		self.name = 'echo server'
		
	def __call__(self,upRead,upWrite,downRead,downWrite):		
		while True:
			req = downRead.get()
			print '%s - request: %s' % (self.name,req)
			
			res = 'echo '+req
			downWrite.put(res)
			print '%s - response: %s' % (self.name,res)
			
class EchoClient(object):

	def __init__(self):
		self.name = 'echo client'
		
	def __call__(self,upRead,upWrite,downRead,downWrite):
		messages = ['hello','world','burek']
		for m in cycle(messages):
			downWrite.put(m)
			print '%s - request: %s' % (self.name,m)
			res = downRead.get()
			print '%s - response: %s' % (self.name,res)

if __name__ == '__main__':
	pass
