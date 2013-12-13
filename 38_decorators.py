
def mydec(func):
    def wrapper(*args,**kwargs):
        print 'mydec - called func!'
        return func(*args,**kwargs)
    return wrapper

class myclassdec(object):

    def __init__(self,i=1,j=5):
        self.i = i
        self.j = j

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print 'myclassdec - called func i=%d,j=%d!' % (self.i,self.j)
            return func(*args,**kwargs)
        return wrapper
        
class myclassdec2(object):

    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        print 'args',args,kwargs
        print 'myclassdec2 - called func!'
        return self.func(*args,**kwargs)
   
@mydec
def func(a,b,c):
    print a,b,c

@myclassdec(i=1,j=2)
def func2(a,b,c):
    print a,b,c
    
def logged(_class):
    cons = _class.__init__
    def __init__w_log(*args,**kwargs):
        cons(*args,**kwargs)
        print 'logged - instance created!'
    _class.__init__ = __init__w_log
    return _class
    
def logged2(_class):
    def wrapper(*args,**kwargs):
        c = _class(*args,**kwargs)
        print 'logged2 - instance created'
        return c
    return wrapper

@logged2
class Autobus(object):
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    @mydec
    def func1(self):
        print self.a,self.b,self.c
    
    @myclassdec(i=3,j=4)
    def func2(self):
        print self.a,self.b,self.c
        
    @myclassdec2
    def func3(self):
        print self.a,self.b,self.c
    
func(1,2,3)
func2(4,5,6)

a = Autobus(7,8,9)
a.func1()
a.func2()
#a.func3() #doesn't work


def singleton(_class):
    class wrapper_class(object):
        def __init__(self):
            self.instance = None
            
        def __call__(self,*args,**kwargs):
            if self.instance:
                return self.instance
            else:
                self.instance = _class(*args,**kwargs)
                return self.instance
    return wrapper_class()

@singleton
class Person(object):
    
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
        
@singleton
class Router(object):

    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
    
a = Person('Toni')
b = Person('Anja')

c = Router('R1')
d = Router('R2')

print a,b
print c,d
    