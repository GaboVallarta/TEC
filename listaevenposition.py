n=int(input("De cuántos será la lista? "))
lista=[]
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    for i in range(n):
        if lista[i]%2==0:
            print(f"position {i}: = value: {lista[i]}")