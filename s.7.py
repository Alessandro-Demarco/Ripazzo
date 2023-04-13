import random
l=[]
s=[1,2,3]
k=0
for x in range(2000000):
    p=random.randint(0,100)
    l.append(p)
for i in range(x-len(s)+1):
    if s==l[i:i+len(s)]:
        k+=1
#print(l)
print("La Combinazione 1,2,3 Si Trova",k,"Volte")