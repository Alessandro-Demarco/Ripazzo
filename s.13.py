l1=["aple","banana","cherry","date"]
l2=["banana","date","flag","grape"]
d={}
for x in l1:
    if x not in l2:
       print(x)
for x in l2:
    if x not in l1:
       print(x)
sl1=set(l1)
sl2=set(l2)
print(sl1.union(sl2))
print(sl1.intersection(sl2))