s=0
#i=0
l=[]
#while i<5:
for x in range (10):
    a=int(input("Numero:"))
    #if a>0:
    l.append(a)
    s=s+a
        #i=i+1
    #else:
    print(x)
      #print("Non E Un Numero Positivo") 
print("La Somma E",s)
for x in l:
    print(x)