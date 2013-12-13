from abc import ABCMeta,abstractmethod

class MyIter(object):

	def __init__(self,item):
		self._item = item
		self._len = len(item)
		self._value = 0
		
	def next(self):
		if self._value >= self._len:
			raise StopIteration
		else:
			return self._item[self._value]
		self._value+=1	

class MyString(object):
	
	def __init__(self,val):
		self.__dict__['array'] = list(val)
		self.random = 1
	
	def __getitem__(self,i):
		if isinstance(i,int):
			return self.array[i]
		elif isinstance(i,slice):
			return ''.join(self.array[i])
			
	def __setitem__(self,i,value):
		if isinstance(i,int):
			self.array[i] = value
		elif isinstance(i,slice):
			self.array[i] = list(value)
	
	def __int__(self):
		v = [s for s in self.array if s.isdigit()]
		return int(''.join(v))
		
	def __index__(self):
		return self.__int__()
		
	def __bin__(self):
		return bin(int(self))
		
	def __hex__(self):
		return hex(int(self))
		
	def __oct__(self):
		return oct(int(self))
	
	def __len__(self):
		return len(self.array)
		
	def __bool__(self):
		return self.__len__() > 0
		
	def __nonzero__(self):
		return self.__bool__()
		
	def __iadd__(self,value):
		self.__dict__['array'].extend(value)
		return self
	
	def __contains__(self,value):
		return value in self.array
		
	def __getattr__(self,attr):
		print 'accessing undefined attr!'
		
	def __setattr__(self,attr,value):
		if attr == 'array':
			raise AttributeError('setting array not allowed')
		return super(MyString,self).__setattr__(attr,value)
	
	def __getattribute__(self,attr):
		#print 'accessing attribute '+attr
		return super(MyString,self).__getattribute__(attr)
	
	def __str__(self):
		return ''.join(self.array)
		
	def __repr__(self):
		return self.__str__()
		
	def __call__(self,*pargs,**kwargs):
		print 'calling! '+str(self)
		
	def __del__(self):
		print 'garbage collecting!'
		
		
a = MyString('Hello World!')
print a

a[1] = '5'
a[5:6] = ' Auto123bus '

print a

print a[1]
print a[0:5]

print len(a)

print int(a)
print bin(a)
print oct(a)
print hex(a)

i = iter(a)
j = iter(a)

next(i)
next(i)

print list(i),list(j)

print list(a)
for s in a:
	print s
	
print bool(a) == True
print '5' in a

try:
	a.array = 'whatever'
except AttributeError as e:
	print e
a.random = 3
print a.random

a.nonexisting

a+='A'
print a

a()

a = 'Hello'
print a
