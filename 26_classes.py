from abc import ABCMeta,abstractmethod

class Person(object):
	
	__metaclass__ = ABCMeta
	counter=0
	
	@abstractmethod
	def talk(self):
		print 'Hello!'

	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname
	
	def __str__(self):
		attrs = ['%s=%s'% (k,self.__dict__[k]) for k in sorted(self.__dict__.keys())]
		return '%s(%s)' % (self.__class__.__name__,','.join(attrs))
		
	def __repr__(self):
		return self.__str__()

class Worker(Person):

	def talk(self):
		super(Worker,self).talk()
		print 'I\'m at work!'
		
class Child(Person):
	
	def talk(self):
		super(Child,self).talk()
		print 'I\'m a child!'
		
a = Worker('Petar','Peric')
b = Child('Giuseppe','Rossi')

print a
print b

a.counter = 5
Person.counter = 2;

print Person.counter
print a.counter
print b.counter

print b.__class__
print Person.__bases__

print a.__dict__.keys()
print b.__dict__.keys()
print Person.__dict__.keys()

a.talk()
b.talk()


print getattr(b,'firstname')

print a
print b

import pickle

data = (a,b)
print data
s = pickle.dumps(data)
print type(s)
print pickle.loads(s)


import shelve
db = shelve.open('shelve_db')
#db['pero'] = a
#db['marco'] = b
print db['pero']
print db['marco']
db.close()