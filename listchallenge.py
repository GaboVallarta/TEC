def llena_lista_texto(t):
    lista=[]
    for i in range(t):
        palabra=input("Ingrese un nombre: ")
        lista.append(palabra)
    return lista
def llena_lista_edades(t):
    lista=[]
    for i in range(t):
        edad=int(input("Ingrese una edad: "))
        lista.append(edad)
    return lista

# def combina_listas(nombres, edades):
#     for i in range(min(len(nombres), len(edades))):
#         print(f"{nombres[i]} tiene {edades[i]} años")
def combina_listas(nombres, edades):
    lista_combinada=[]
    size=max(len(nombres), len(edades))
    for i in range(size):
        #lista_combinada.append((nombres[i] if i<len(nombres) else "N/A", edades[i] if i<len(edades) else "N/A"))
        lista_combinada.append(nombres[i])
        lista_combinada.append(edades[i])
    print(lista_combinada)

def main():
    n=int(input("De cuántos será la lista de nombres? "))
    m=int(input("De cuántos será la lista de edades? "))
    if n<=0 or m<=0:
        print("No se puede")
    else:
        print(5*"-")
        nombres=llena_lista_texto(n)
        print(5*"-")
        edades=llena_lista_edades(m)
        print(5*"-")
        print(nombres)
        print(edades)
        combina_listas(nombres, edades)

    