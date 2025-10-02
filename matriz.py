import random 
def llena_matriz(ren, col):
    matriz=[]
    for i in range (ren):
        lista=[]
        for j in range (col):
            dato=random.randint(1,5)
            lista.append(dato)
        matriz.append(lista)
    return matriz

def imprime_lista(matriz):
    for lista in matriz:
        for elemento in lista:
            print(elemento, end="\t")
        print()


def suma_renglon(matriz,ren,col):
    total=0
    for i in range(ren):
        for j in range(col):
            total+=matriz[i][j]
        print("El total del renglon", i+1, "es ", total)
        total=0

def suma_columna(matriz,ren,col):
    total=0
    
    print()



def main():
    renglon=int(input("Dame el numero de renglones: "))
    columna=int(input("Dame el numero de columnas: "))
    mi_matriz=llena_matriz(renglon,columna)
    imprime_lista(mi_matriz)
    suma_renglon(mi_matriz,renglon,columna)
    suma_columna(mi_matriz,renglon,columna)
main()