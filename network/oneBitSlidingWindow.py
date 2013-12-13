import time
import random
from threading import Timer
from Queue import Empty

from frame import Frame
from channel import Channel

TIMEOUT = 5

class Node(object):

	def __init__(self,name,messages):
		self.name = name
		self.messagesout = map(str,messages)
		self.messagesout.reverse()
		self.messagesin = []
		
	def __call__(self,qRead,qWrite):
		
		time.sleep(random.random())
		
		next_seq_to_send = 0
		next_seq_expected = 0
		
		m = self.messagesout.pop()
		
		while True:
			try:
				fin = qRead.get(timeout=TIMEOUT)
				if fin.isvalid():
					if fin.seq == next_seq_expected:
						self.messagesin.append(fin.packet)
						next_seq_expected = (next_seq_expected+1)%2
						print '%s recieved: %s' % (self.name,''.join(self.messagesin))
					if fin.ack == next_seq_to_send:
						m = self.messagesout.pop()
						next_seq_to_send = (next_seq_to_send+1)%2
			except Empty:
				pass
			
			fout = Frame(m,seq=next_seq_to_send,ack=(next_seq_expected+1)%2)
			qWrite.put(fout)
			print '%s sent %s' % (self.name,fout)

if __name__ == '__main__':

	nodeA = Node('A',range(1,100))
	nodeB = Node('B',(chr(ord('A')+i) for i in range(0,100)))
	
	Channel(nodeA,nodeB,lossrate=0.15,damagerate=0.15,latency=0.4).start()
	#Channel(nodeA,nodeB,lossrate=0.0,damagerate=0.0,latency=0.4).start()