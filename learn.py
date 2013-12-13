# coding: utf8

from imp import reload

print 'string rep!' * 5

#rin = raw_input('Input raw input?')
#print rin

#rin2 = input('Input?')
#print rin2

import script1

reload(script1)

print dir(script1)

import sys
print sys.path

a = set([1,2,3,4])
print a
print len(a)


x=2
y=100
r=x ** y
print '%d^%d=%d %s^%s=%s'%(x,y,r,type(x),type(y),type(r))

try:
	x = 'abcdefghijk'
	x[1]='x'
except TypeError,e:
	print e
	
#help('a'.lstrip)
print 'a'.lstrip.__doc__

a=r'auto\bus'
print a,type(a)
b=u'helloworld'
print b,type(b)
c='ŠĐŽĆČčćžđš'
print c,type(c)


g = (x*2 for x in range(1,10))
print g,type(g)
for x in g:
	print x

it = ['a','bb','ccc','d']
m = map(len,it)
print m

list = ['ccccc','AAAAA','bbbbb','DDDDD']
print sorted(list,reverse=False,key=str.lower)
print list

s = {1,2,3,4}
t = {4,5,6}
print s-t,s|t,s&t

from fractions import Fraction
a = Fraction(1,3)
b = 1
print a+b

f = open('sometext.txt','r')
r = f.readlines()
print type(r)
f.close()

