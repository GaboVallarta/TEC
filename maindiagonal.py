"""
este programa manipula matrices
"""
import random
def llena_matriz(n):
    matriz=[]
    for i in range(n):
        lista=[]
        for j in range(n):
            dato=random.randint(1,9)
            lista.append(dato)
        matriz.append(lista)
    return matriz


def obtiene_diagonal(matriz):
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i==j:
                lista.append(matriz[i][j])
        print()
    print(f'La diagonal principal es: {lista}')

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'{matriz[i][j]:3}',end=' ')
        print()

def main():
    print("este programa llena una matriz a partir de la diagonal de un amatriz")
    mi_matriz=llena_matriz(4)
    obtiene_diagonal(mi_matriz)
    imprime_matriz(mi_matriz)


main()