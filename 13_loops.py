import copy

l = ['hello','world',10,15,5,3.4]
e = enumerate(l)
e2 = enumerate(l)
print dict(e)
print list(e2)

print [x+y for x in "helloworld" for y in "1234567" if int(y) % 2 == 0]

a = ['A','b','C','d']
b = ['e','f','g']

print map(str.upper,a)
print zip(a,b)
print filter(str.isupper,a);

import operator
print reduce(operator.add,a)

list = ['ccccc1','AAAAA4','bbbb2','DDDD3']
print sorted(list,reverse=False,key=str.lower)

def mycmp(a,b):
	return int(a[-1]).__cmp__(int(b[-1]))

print sorted(list,reverse=True,cmp = mycmp)

myargs=['hello',1,'world',2]

def foo(str1,int1,str2,int2):
	print str1,str2,int1,int2
	
#foo(myargs)
foo(*myargs)

a = (1,2,3)
b = (4,5,6)

print zip(a,b)

print zip(*zip(a,b)) #unzip a zip

r = range(1,20,3)
print type(r)

d = {1:'A',2:'B',3:'C'}
print d.keys()
print d.items()
print d.values()