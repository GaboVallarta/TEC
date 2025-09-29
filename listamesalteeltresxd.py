n=int(input("De cuántos será la lista? "))
lista=[]
mean=0
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    for i in range(n):
        mean=mean+lista[i]
    mean=mean/n
    print (mean)