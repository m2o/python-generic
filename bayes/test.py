import Pmf

pmf1 = Pmf.MakePmfFromList(range(0,7))
pmf2 = Pmf.MakePmfFromList(range(0,11))

#for value,prob in p1.Items():
    #print value,prob

ptot = 0    
    
for v1,p1 in pmf1.Items():
    for v2,p2 in pmf2.Items():
        if v2 > v1:
            ptot += p1*p2

print ptot
