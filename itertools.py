import itertools

iter_count = itertools.count(1)
iter_cycle = itertools.cycle((1,2,'A','B'))

n=0
while n < 10:
    print next(iter_count)
    n+=1
    
n=0
while n < 10:
    print next(iter_cycle)
    n+=1
    
    
print list(itertools.repeat('Autobus',4))
print list(itertools.chain([1,2,3],(4,5,6),set([7]),'8910'))
print list(itertools.compress([1,2,3,4,5,6,7,8],[True,False,True]))

import random
data = [random.randint(0,100) for i in range(0,1000)]
keyfunc = lambda x: int(float(x)/10)
sorted_data = sorted(data,key=keyfunc)
print [(k,list(g)) for k,g in itertools.groupby(sorted_data,key=keyfunc)]

print ''
print list(itertools.ifilter(lambda x:x>10,range(0,21)))
print list(itertools.ifilterfalse(lambda x:x>10,range(0,21)))

data = range(0,101)
print data[3:97:12]
print list(itertools.islice(data,3,97,12))

print list(itertools.imap(pow,[1,2,3,4],[1,2,3,4,5,6,7]))
print list(itertools.imap(pow,itertools.count(1),[1,2,3,4,5,6,7]))
print list(itertools.imap(pow,range(1,11),itertools.repeat(2)))

print list(itertools.imap(lambda a,b: a*b,['a','b','c','d'],[1,2,3,4]))
print list(itertools.starmap(lambda a,b: a*b,[('a',1),('b',2),('c',3),('d',4)]))

#tee
iter = (i for i in range(0,11))
print list(iter)
print list(iter)

iter = (i for i in range(0,11))
(iter1,iter2) = itertools.tee(iter,2)
print list(iter1)
print list(iter2)

#izip
print list(itertools.izip([1,2,3,4],['a','b','c']))

#izip_longest
print list(itertools.izip_longest([1,2,3,4],['a','b','c'],fillvalue='-1'))

#product
print list(itertools.product([1,2,3],['a','b','c']))
print list(itertools.product([0,1],repeat=3))

#permutations
print list(itertools.permutations([1,2,3,4,5],r=2))

#combinations
print list(itertools.combinations([1,2,3,4,5],r=2))

#combinations_with_replacement
print list(itertools.combinations_with_replacement([1,2,3,4,5],r=2))