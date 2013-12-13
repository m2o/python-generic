import time
import random
from Queue import Empty
from multiprocessing import Process, Queue

from frame import Frame

QUEUE_MAX_SIZE = 10

class Channel2(object):
	def __init__(self,latency=0.5,lossrate=0.0,damagerate=0.0):
		self.lossrate = lossrate
		self.damagerate = damagerate
		self.latency = latency
		self.name = 'channel'
		
	def __call__(self,aRead,aWrite,bRead,bWrite):
			
		while True:
			for (direction,qRead,qWrite) in (('A->B',aRead,bWrite),('B->A',bRead,aWrite)):
				try:
					f = qRead.get(block=False)
					#print 'channel recieved from A:',mA
				
					r = random.random()
					if r <= self.lossrate:
						print 'ERROR:channel lost frame ',f
						f = None
					elif r <= self.lossrate + self.damagerate:
						f.damage()
						print 'ERROR:channel damaged frame ',f

					if f:
						qWrite.put(f)
						#print '%s %s - passing message %s' % (self.name,direction,f)
						#print 'channel sent to B:',mA

				except Empty:
					pass
				
			time.sleep(self.latency)
		
class Channel(object):
	def __init__(self,runA,runB,latency=0.5,lossrate=0.0,damagerate=0.0):
		self.runA = runA
		self.runB = runB
		self.lossrate = lossrate
		self.damagerate = damagerate
		self.latency = latency
		
	def start(self):
		qAC = Queue(QUEUE_MAX_SIZE)
		qCA = Queue(QUEUE_MAX_SIZE)
		qBC = Queue(QUEUE_MAX_SIZE)
		qCB = Queue(QUEUE_MAX_SIZE)
		
		pA = Process(target=self.runA, args=(qCA,qAC))
		pB = Process(target=self.runB, args=(qCB,qBC))
		
		pA.start()
		pB.start()
		
		import signal
		import sys
		def signal_handler(signal, frame):
				print 'You pressed Ctrl+C!'
				pA.terminate()
				pB.terminate()
				sys.exit(0)
		signal.signal(signal.SIGINT, signal_handler)

		while True:
		
			for (direction,qRead,qWrite) in (('A->B',qAC,qCB),('B->A',qBC,qCA)):
				try:
					f = qRead.get(block=False)
					#print 'channel recieved from A:',mA
				
					r = random.random()
					if r <= self.lossrate:
						print 'ERROR:channel lost frame ',f
						f = None
					elif r <= self.lossrate + self.damagerate:
						f.damage()
						print 'ERROR:channel damaged frame ',f

					if f:
						qWrite.put(f)
						print '%s %s - passing message %s' % (self.name,direction,f)
						#print 'channel sent to B:',mA

				except Empty:
					pass
				
			time.sleep(self.latency)
