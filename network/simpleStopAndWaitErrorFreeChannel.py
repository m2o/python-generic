import time

from frame import Frame
from channel import Channel

def nodeA(qRead,qWrite):
	for i in range(1,10):
		m = "burek %s" % (i,)
		f = Frame(m)
		qWrite.put(f)
		print 'a sent: ',m
		
		qRead.get()
		print 'a recieved ack'
	
def nodeB(qRead,qWrite):
	while True:
		f = qRead.get()
		m = f.packet
		print 'b recieved: ',m
		
		f = Frame(None)
		qWrite.put(f)
		print 'b sent ack'

if __name__ == '__main__':
	Channel(nodeA,nodeB).start()
	