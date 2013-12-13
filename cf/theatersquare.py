from __future__ import division

import sys
from math import ceil

readints = lambda : map(int,sys.stdin.readline().split())

(n,m,a) = readints()
nl = int(ceil(m/a))
ml = int(ceil(n/a)) 
tot = nl * ml
print tot
