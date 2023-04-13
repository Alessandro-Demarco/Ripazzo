s=input("Testo:")
l="l"
k=0
for i in range (len(s)):
    if l==s[i:i+len(l)]:
        k+=1
        print("Trovata",l,"Al Posto:",i)
print("La l Si E Stata Inserita",k)