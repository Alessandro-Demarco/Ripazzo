l=input("Testo:")
i=0
d=0
s="l"
k=[]
for x in l:
    i+=1
    if x in ["a","e","i","o","u"]:
       d+=1
       k.append(x)
print("Le Lettere Nel Testo Sonno:",i)
print("Le Vocali Nel Testo Sonno:",d,"E Sonno",k)