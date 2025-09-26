

def calcost(weight): #aquí va descartando precios desde el más bajo hasta que llega a la posibilidad más alta
    costo=0
    if weight<10:
        costo= 100
    elif weight<45:
        costo= 200+25*(weight-10)
    elif weight<90:
        costo= 500+35*(weight-45)
    else:
        costo= 1000+50*(weight-90)
    return costo

def main():
    packages=0
    totcosts=0
    weight=0.0
    go=True #definimos variable go para que esté repitiendo y repitiendo hasta que sea falso
    print("---Welcome ---")
    while go:
        weight=float(input("Enter the weight of the package: "))
        if weight<=0:#si el peso es mejor o igual a 0 se hace falsa la variable go 
            go=False
        else: # si es mayor a 0 entonces calcula el costo mediante la función y guarda el valor en costo
            cost=calcost(weight)
            print(f"The cost of the package is: {cost:,.2f} pesos") # meustra el costo 
            packages+=1
            totcosts+=cost
    print(f"The total number of packages is {packages} with a total cost of {totcosts:,.2f} pesos")#una vez termina el while, sale y muestra el total de paquetes vendidos jutno con el costo total

main()