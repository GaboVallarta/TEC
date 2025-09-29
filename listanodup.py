n=int(input("De cuántos será la lista? "))
lista=[]
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=input("Ingrese un nombre: ")
        lista.append(valor)
    listanodup=[]
    for i in range(n):
        if not lista[i] in listanodup:
            listanodup.append(lista[i])
    print(lista)
    print(listanodup)