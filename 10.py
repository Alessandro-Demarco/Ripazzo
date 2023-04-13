import random
p=random.randint(1,90)
a=int(input("Numero:"))
n=1
s=""
while p!=a:
    if abs(a-p)<5:
        s="Fuoco"
    elif abs(a-p)<10:
        s="Fuochino"
    elif abs(a-p)<15:
        s="Fucherello"
    elif abs(a-p)>=15:
        s="Acqua"
    print(s)
    if a<p:
        print("Il Numero E Piu Grande")
    else:
        print("Il Numero E Piu Piccolo")
    a=int(input("Ritenta:"))
    n+=1
print("Hai Vinto Hai Indovinato Con",n,"Di Tentativi")