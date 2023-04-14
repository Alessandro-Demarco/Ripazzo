def MCD(a,b):
    if a>b:
       return MCD(a-b,b)
    elif a<b:
       return MCD(b,b-a)
    else:
       return(a)
a=int(input("Numero1:"))
b=int(input("Numero2:"))
print(MCD(a,b))