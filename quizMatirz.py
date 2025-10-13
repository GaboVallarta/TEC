"""
Gabriel Vallarta Ramírez a01648413
llenar matriz n rand 1 a 9
se imprimirá con tabulador 
para poner tabulador en el print se utiliza \t
"""

import random

def llena_matriz(n):
    matriz=[]
    lista=[]
    for i in range(0,n,1):
        for j in range(n):
            i=random.randint(1,9)
            lista.append(i)
        matriz.append(lista)
        lista=[]
    return matriz
    
def imprime_matriz(matriz,n):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j],  end= "\t")
        print()


def sum_diag(matriz,n):
    diag=[]
    for i in range(0,n,1):
        for j in range(len(matriz[0])):
            if i==j:
                diag.append(matriz[i][j])
            
    print("la suma de la diagonal es:",sum(diag))




def main():
    print()
    n=int(input("elige de cuanto va a ser la matriz cuadrada"))
    mi_matriz=llena_matriz(n)
    imprime_matriz(mi_matriz,n)
    sum_diag(mi_matriz,n)

main()