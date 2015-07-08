h=[]

for a in 'abc', 'ade':
    b= a[:]  # it seems that b=a is also OK.
    b= a.replace('a','www',1)
    h.append(b)
    
print h
    