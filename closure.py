def make(a,b):
    c = 3
    def wrap(d):
    	return a+b+c+d
    return wrap

m1 = make(1,2)

print m1(4)
print [c.cell_contents for c in m1.__closure__]
