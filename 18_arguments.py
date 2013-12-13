def func1(a=-1,b=-2,c=-3):
	print a,b,c
	
def func2(*args):
	print args
	
def func3(*argl,**argd):
	print argl,argd	

def func4(x,y,**args):
	print x,y,args

func1(1,2,3);
func1(1,2);

args = [10,11]
func1(*args)

argsd = {'b':200,'c':300}
func1(**argsd)

func2(*[1000,2000,3000,4000,5000])

func3(1,2,3,auto=2,prikolica=3)

func4(1,2,a=12,b=13,c=14)

def dispacher(f,*pargs,**kargs):
	print 'dispatching to: %s'%f.__name__
	return f(*pargs,**kargs)
	
dispacher(func4,-2,-4,a=1,b=2,c=3)