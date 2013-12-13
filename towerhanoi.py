n = 10

a = range(n,0,-1)
b = [] 
c = []

def towerhanoi(frm,mid,to,n):
    if n<=0:
        raise ValueError("expected positive integer for n")
    elif n==1:
        to.append(frm.pop())
    else:
        towerhanoi(frm,to,mid,n-1)
        to.append(frm.pop())
        towerhanoi(mid,frm,to,n-1)

if __name__ == '__main__':
    print 'a:',a
    print 'b:',b
    print 'c:',c
    towerhanoi(a,b,c,n)
    print 'a:',a
    print 'b:',b
    print 'c:',c


