""" Jota es la horizontal, i es vertical, en este estamos sumando columnas, normalmente sumamos filas en horizontal"""


def suma_lista(matriz):
    suma=0
    cont=2
    for i in range(0,len(matriz)):
        suma =sum(matriz[i])
        cont=cont+1
        print(f'La suma de la fila {cont} es: {suma}')
        suma=0
#la hizo mal la miss, no funciona bien

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

for i in range(len(matriz)):
    suma_col=0
    for j in range(len(matriz[0])):
        suma_col += matriz[j][i]
    print(f'La suma de la columna {i+1} es: {suma_col}')

suma_lista(matriz)