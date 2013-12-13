class JobAttr(object):
	
	def __get__(self,instance,owner):
		return 'job %s' % instance._job
		
	def __set__(self,instance,value):
		instance._job = value.upper()
		
	def __delete__(self,instance):
		del instance._job
		
class SalaryAttr(object):
	
	def __get__(self,instance,owner):
		return self.salary
		
	def __set__(self,instance,value):
		self.salary = value

class Person(object):

	job = JobAttr()
	salary = SalaryAttr()
	
	def __init__(self,value):
		self._name = value
		
	@property
	def name(self):
		return self._name * 2
	
	@name.setter
	def name(self,value):
		self._name = value * 3
	
	@property
	def age(self):
		return 10
		

p = Person('Toni')
print p.name

p.name = 'Autobus'
print p.name

print p.age
try:
	p.age = 10
except AttributeError,e:
	print e
	
p.job = 'doktor'
print p.job

p2 = Person('Anja')

p.salary = 100
p2.salary = 140

print p.salary
print p2.salary #descripor object is class attribute!

class Thing(object):

	def __str__(self):
		return 'pretty name'
		

class Wrapper(object):

	def __init__(self):
		self.thing = Thing()
		
	def __str__(self):
		return self.thing.__str__()
		
	def __getattribute__(self,attr):
		print 'getattribute %s' % attr
		return object.__getattribute__(self,attr)
		
w = Wrapper()
print w
print w.__str__()
