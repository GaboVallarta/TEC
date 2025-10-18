# f=open(r"C:\Users\adolf\Downloads\office_depot.csv","r",encoding='utf-8')

# f.close()

def imprime_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end="\t")
        print()

def main():
    with open(r"C:\Users\adolf\Downloads\office_depot.csv","r",encoding='utf-8') as archivo:
        contenido=archivo.readlines()#trae todo y hace una lista
    print(contenido)

    matriz=[]
    for linea in contenido:
        lista=linea.strip().split(",") # quitar salto de linea y separar por comas
        matriz.append(lista)
        print(matriz)
        imprime_matriz(matriz)

    #separar matriz

    encabezado=matriz[0]
    print(encabezado)
    
main()