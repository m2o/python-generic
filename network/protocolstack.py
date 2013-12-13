import signal
import sys
from multiprocessing import Process, Queue

QUEUE_MAX_SIZE = 100

class ProtocolStack(object):
	def __init__(self,stackA,stackB,channel):
		self.stackA = stackA
		self.stackB = stackB
		self.channel = channel
	
		self.process_stackA = connectstack(stackA)
		self.process_stackB = connectstack(stackB)
	
		last_a = self.process_stackA[-1]
		last_b = self.process_stackB[-1]
		
		channel_a_read = last_a['queues']['downWrite']
		channel_a_write = last_a['queues']['downRead']
		channel_b_read = last_b['queues']['downWrite']
		channel_b_write = last_b['queues']['downRead']
		
		self.process_channel = Process(target=channel, args=(channel_a_read,channel_a_write,channel_b_read,channel_b_write))
		
		self.processes = [self.process_channel]
		self.processes.extend(d['process'] for d in self.process_stackA)
		self.processes.extend(d['process'] for d in self.process_stackB)
		
	def start(self):
		def signal_handler(signal, frame):
			print 'You pressed Ctrl+C!'
			[p.terminate() for p in self.processes]
			sys.exit(0)
		signal.signal(signal.SIGINT, signal_handler)
		
		[p.start() for p in self.processes]
		
		#self.process_stackA[0]['queues']['upRead'].put('burek')
		#print(self.process_stackA[0]['queues']['upWrite'].get())
		
		self.process_channel.join()

def connectstack(stack):
	
	process_stack = []
	
	upRead = Queue(QUEUE_MAX_SIZE)
	upWrite = Queue(QUEUE_MAX_SIZE)
	downRead = Queue(QUEUE_MAX_SIZE)
	downWrite = Queue(QUEUE_MAX_SIZE)	
	
	for layer in stack:
		layer_process = Process(target=layer, args=(upRead,upWrite,downRead,downWrite))
		process_stack.append({'process':layer_process,
		                      'queues':{'upRead':upRead,
		                                'upWrite':upWrite,
		                                'downRead':downRead,
		                                'downWrite':downWrite}
		                      })
		
		upRead = downWrite
		upWrite = downRead
		downRead = Queue(QUEUE_MAX_SIZE)
		downWrite = Queue(QUEUE_MAX_SIZE)
		
	return process_stack
		
if __name__ == '__main__':
	
	from layer import Layer,EchoClient,EchoServer
	from channel import Channel2
	
	stackA = [Layer('layer_A_%d' % i) for i in range(5,0,-1)]
	stackB = [Layer('layer_B_%d' % i) for i in range(5,0,-1)]

	stackA.insert(0,EchoClient())
	stackB.insert(0,EchoServer())
	
	channel = Channel2()
	
	ProtocolStack(stackA,stackB,channel).start()
	    
	    
	
		
		