class Monoid(object):

    def __init__(self,null,lift,op):
        self.null = null
        self.lift = lift
        self.op = op
        
    def __call__(self,*args):
        return self.fold(args)
       
    def fold(self,args):
        args = map(self.lift,args)
        return reduce(self.op,args,self.null)
        
    def star(self):
        return Monoid(self.null,self.fold,self.op)
        
    def reverse(self):
        return Monoid(self.null,self.lift,lambda a,b: self.op(b,a))
        
summ = Monoid(0,int,lambda a,b:a+b)
joinm = Monoid('',str,lambda a,b:a+b)
lenm = Monoid(0,lambda x:1,lambda a,b:a+b)
listm = Monoid([],list,lambda a,b:a+b)


print summ(0,1,10,20)
print joinm('b',1,'a',20)
print lenm(*range(0,100))

print joinm.star()([1,2,3,4],(5,6,7,8,9),set([10]))

_in = [['a','b','c'],['d','e'],['f'],[]]
print listm.star()(_in)

print joinm('b',1,'a',20)
print joinm.reverse()('b',1,'a',20)