import time
from threading import Timer
from Queue import Empty

from frame import Frame
from channel import Channel

TIMEOUT = 1

def nodeA(qRead,qWrite):
	
	next_seq_to_send = 0
	
	messages = iter(["%s" % (i,) for i in range(1,100)])
	m = next(messages)
	
	while m is not None:
		f = Frame(m,seq=next_seq_to_send)
		qWrite.put(f)
		print 'a sent: ',f
		
		try:
			fack = qRead.get(timeout=TIMEOUT)
			if fack.isvalid():
				#print 'a recieved: ',fack
				m = next(messages)
				next_seq_to_send = (next_seq_to_send+1)%2
		except Empty:
			pass
	
def nodeB(qRead,qWrite):

	next_seq_expected = 0
	
	messages = []

	while True:
		f = qRead.get()
		if f.isvalid():
			if f.seq == next_seq_expected:
				m = f.packet
				#print 'b recieved: ',f
				messages.append(m)
				next_seq_expected = (next_seq_expected+1)%2
			
			fack = Frame(None,ack=f.seq)
			qWrite.put(fack)
			print 'b sent: ',fack
		print 'b message:',''.join(messages)

if __name__ == '__main__':
	Channel(nodeA,nodeB,lossrate=0.15,damagerate=0.15,latency=0.4).start()