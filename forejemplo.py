def prom():
    suma = 0
    for num in range(1,6):
        suma=suma+num
    promedio=suma/num
    print(f"La suma de los números del 1 al 5 es: {suma}")
    print(f"El promedio de los números del 1 al 5 es: {promedio}:.2f")


def main():
    prom() 

main()