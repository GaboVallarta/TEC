n=int(input("De cuántos será la lista? "))
lista=[]
odd=[]
even=[]
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
        if valor%2==0:
            even.append(valor)
        else:
            odd.append(valor)
    print("original")
    print(lista)
    print("even")
    print(even)
    print("odd")
    print(odd)

    