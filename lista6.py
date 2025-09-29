lista=[]
listb=[]
listtotal=[]

n=int(input("De cuántos será la lista? "))
if n<=0:
    print("No se puede")
else:
    for i in range(0,n,1):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    for i in range(0,n,1):
        valor=int(input("Ingrese un valor: "))
        listb.append(valor)
    for i in range(0,n,1):
        listtotal.append(lista[i]+listb[i])
    print(listtotal)