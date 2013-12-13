# coding: utf8

a = 2+4j;
b= 1+3j;
c = complex(2,4)
print a,b,a+b,c,type(a)

_bin = 0b1011;
print _bin

_hex = 0x1EA6;
print _hex

_oct = 0o1347
print _oct

print 3 if False else 4;

somestr = "abcdefghij"
print somestr[2:7]
print somestr[2:7:2]
print somestr[slice(2,7,2)]

print 9.5/4
print 9.5//4

from decimal import Decimal
res = Decimal('0.01')+Decimal('0.03')
print res,type(res)

from fractions import Fraction

res = Fraction(1,4)+Fraction(1,10)
print res,type(res)
print (0.4).as_integer_ratio()