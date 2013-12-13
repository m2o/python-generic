import sys

def myfunc(a,b,*pargs,**kargs):
	v=2
	l=4
	print a,b,pargs,kargs

myfunc(1,2,3,4,5,x=1,y=3)
print dir(myfunc.__code__)

print myfunc.__code__.co_argcount
print myfunc.__code__.co_cellvars
print myfunc.__code__.co_varnames

def func1(var):
	func1.count+=1
	print func1.count,var
	
func1.count=1
func1(1111)
func1(2222)
func1(10)
func1(2)


bases = (1,2,3,4)
powers = (-1,-2,-3,-4)

print map(pow,bases,powers)
map(lambda a,b: sys.stdout.write(str(a**b)+' '),bases,powers)
print ''

print reduce(lambda cur,item: cur+item,bases)