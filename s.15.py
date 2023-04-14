l=["uno","due","uno","uno","due"]
d={}
for p in l:
    if p in d.keys():
        v=d[p]
        d[p]=v+1
    else:
        d[p]=1
print(d)
#uno:3
#due:2
