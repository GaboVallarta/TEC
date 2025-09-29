n=int(input("De cuántos será la lista? "))
lista=[]
if n<=0:
    print("No se puede")
else:
    for i in range(n):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    for i in range(-1,n+1,1):
        print(f"lista[{-i}] = {lista[-i]}")