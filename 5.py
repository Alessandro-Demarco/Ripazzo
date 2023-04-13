print("Menu:")
print("A Orecciette Con Cime Di Rapa 10€")
print("B Pasta Al Pesto 11€")
print("C Spagetti Alla Carbonara 12€")
print("D Pasta Al Pomodoro 13€")
s=input("Cosa Vuoi Ordinare:")
d=int(input("Per Quande Persone:"))
if s=="A":
    i=10
elif s=="B":
   i=11
elif s=="C":
    i=12
elif s=="D":
    i=13
d=d*i
print("Sono",d,"€")
print("Grazie Per Ordine")