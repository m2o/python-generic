class A(object):
	pass
	
class B(list):
	pass

a = A()
b = B()

print type(a)
print type(A)

print type(b)
print type(B)

print type(list)


class Person(object):
	__slots__ = ['name','age']
	
	population = 0
	
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
		Person.population += 1
		
	@staticmethod
	def current_population():
		return Person.population
		
		
p = Person('Toni',100)
p.name = 'A'
p.age = 110
try:
	p.sex = 'm'
except AttributeError,e:
	print e
	
p2 = Person('Anja',100)

print p.current_population()

def counter(_class):	
	_class.counter = 0
	return _class
	
@counter
class House(object):
	pass
	
h = House()

print h.counter
h.counter = 100
print House.counter
