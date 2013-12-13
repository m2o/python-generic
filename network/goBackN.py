import time
import random
from Queue import Empty
from threading import Timer

from frame import Frame

def between(a,b,c):
	return ((a <= b) and (b < c)) or\
	        ((c < a) and (a <= b)) or\
	        ((b < c) and (c < a))

class GoBackNProtocolDataLinkLayer(object):

	def __init__(self,name,maxseq=5,timeout=1):
		self.name = name
		self.maxseq = maxseq
		self.timeout = timeout
		
	def inc(self,i):
		return (i+1)%(self.maxseq+1)
		
	def __call__(self,upRead,upWrite,downRead,downWrite):
		
		time.sleep(random.random())
		
		message_buffer = [None for i in range(0,self.maxseq+2)]
		timers = [None for i in range(0,self.maxseq+2)]
		
		n_buffered = 0
		next_seq_to_send = 0
		next_seq_expected = 0
		ack_expected = 0
		
		def send(message,_seq,_seq_expected):
			outframe = Frame(message,seq=_seq,ack=(_seq_expected+self.maxseq)%(self.maxseq+1))
			downWrite.put(outframe)
			timers[_seq] = time.time()
			#print '%s - sent %s' % (self.name,outframe)
			
		def ontimeout():
			#print '%s - timeout ack_expected:%d n_buffered:%d' % (self.name,ack_expected,n_buffered)
			start_seq = ack_expected
			for i in range(0,n_buffered):
				current_seq = (start_seq+i) % (self.maxseq+1)
				outmessage = message_buffer[current_seq]
				send(outmessage,current_seq,next_seq_expected)
		
		while True:
			if n_buffered < self.maxseq:
				try:
					outmessage = upRead.get(block=False)
					message_buffer[next_seq_to_send] = outmessage
					n_buffered += 1
					send(outmessage,next_seq_to_send,next_seq_expected)
					next_seq_to_send = self.inc(next_seq_to_send)
				except Empty:
					pass
			try:
				frameIn = downRead.get(block=False)
				if frameIn.isvalid():

					#print '%s - frameIn.seq:%d next_seq_expected:%d' % (self.name,frameIn.seq,next_seq_expected)
					
					if frameIn.seq == next_seq_expected:
						upWrite.put(frameIn.packet)
						next_seq_expected = self.inc(next_seq_expected)
						#print '%s - recieved %s' % (self.name,frameIn)
					
					#print '%s - ack_expected: %d frameIn.ack:%d next_seq_to_send:%d' % (self.name,ack_expected,frameIn.ack,next_seq_to_send)
					while between(ack_expected,frameIn.ack,next_seq_to_send):
						#print '%s - acknowledged %d' % (self.name,ack_expected)
						timers[ack_expected] = None
						n_buffered -= 1
						ack_expected = self.inc(ack_expected)
			except Empty:
				pass
			
			now = time.time()
			timeout = None
			for i in range(0,self.maxseq+2):
				if timers[i] and timers[i]+self.timeout < now:
					timers[i]+=self.timeout
					timeout = True
			if timeout:
				ontimeout()
			

if __name__ == '__main__':
	
	from layer import Layer,NetworkLayer
	from channel import Channel2
	from protocolstack import ProtocolStack
	
	stackA = []
	stackB = []
	
	stackA.append(NetworkLayer('network_layer_A',list(range(1,100))))
	stackA.append(GoBackNProtocolDataLinkLayer('data_link_layer_A'))
	
	stackB.append(NetworkLayer('network_layer_B',list(range(100,200))))
	stackB.append(GoBackNProtocolDataLinkLayer('data_link_layer_B'))

	channel = Channel2(latency=0.1,lossrate=0.1,damagerate=0.0)
	
	ProtocolStack(stackA,stackB,channel).start()