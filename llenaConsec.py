def llena_conescutivos(n,c):
    cont=1
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(c):
            dato=cont
            lista.append(dato)
            cont=cont+1
        matriz.append(lista)
    return matriz

def main():
    print("este programa")
    r=int(input("ingrese un numero: "))
    c=int(input("ingrese un numero: "))
    mi_matriz=llena_conescutivos(r,c)