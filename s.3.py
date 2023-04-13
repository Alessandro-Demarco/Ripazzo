i=0
mag=int(input("Numero:"))
for x in range(9):
    n=int(input("Numero:"))
    if n>mag:
        i+=1
    mag=n
print("Numero Di Volte Maggiore",i)