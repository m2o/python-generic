print 'else!'

#loops - else
for i in range(0,5):
    print i
else:
    print 'else #1 executed'

for i in range(0,5):
    print i
    if i==3:
        break	
else:
    print 'else #2 executed'

#try-except-else

class A:
    def work(self):
        raise IndexError()

try:
    l = []
    l[0].work()
except IndexError:
    print 'executing #1 except'

try:
    l = [A()]
    l[0].work()
except IndexError:
    print 'executing #2 except (bad!)'

try:
    l = [A()]
    i = l[0]
except IndexError:
    print 'executing #3 except'
else:
    print 'else #3 executed'
    i.work() #raises exception
finally:
    print 'executing finally'

