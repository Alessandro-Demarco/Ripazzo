import random
p=random.randint(1,90)
a=int(input("Numero:"))
n=1
while p!=a:
    if a<p:
        print("Il Numero E Piu Grande")
    else:
        print("Il Numero E Piu Piccolo")
    a=int(input("Ritenta:"))
    n+=1
print("Hai Vinto Hai Indovinato Con",n,"Di Tentativi")