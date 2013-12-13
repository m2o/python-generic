def fibo(n):
    a,b = (0,1)
    for i in range(0,n):
        a,b = (b,a+b)
        yield a
    
print list(fibo(15))

def func():
    y = 0;
    for i in range(0,10):
        r = i+y
        y = yield r

g = func()
print next(g)

print g.send(10)
print g.send(20)


g2 = (x**2 for x in range(1,10))
print g2
print list(g2)