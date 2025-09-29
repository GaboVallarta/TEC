import math 
n=int(input("De cuántos será la lista? "))
lista=[]
square=[]
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
        square.append(math.pow(valor,2))
    print(lista)
    print(square)