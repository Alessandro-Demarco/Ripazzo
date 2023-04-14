import random
l=[]
d={}
for x in range(0,1000000,1):
    p=random.randint(1,20)
    l.append(p)
for o in l:
    if o in d.keys():
        v=d[o]
        d[o]=o*o
    else:
        d[o]=1
print(d)