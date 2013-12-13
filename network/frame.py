import random
import hashlib

class Frame(object):
	def __init__(self,packet,seq=None,ack=None):
		self.packet = packet
		self.hash = hash(packet)
		self.seq = seq
		self.ack = ack
		
	def damage(self):
		self.hash+='_'
		
	def isvalid(self):
		return self.hash == hash(self.packet)
		
	def __str__(self):
		return '(%r,seq=%s,ack=%s)' % (self.packet,self.seq,self.ack)
		
def hash(value):
	m = hashlib.md5()
	m.update(str(value) if value is not None else '')
	return m.digest()