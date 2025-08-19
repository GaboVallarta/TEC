
print("This program calculates the total prices of items with taxes")
cant_articulos=int(input("Enter the number of items: "))  
precio=float(input("Enter the total price of each item: $"))
subtotal=cant_articulos*precio
impuestos=subtotal*0.16
total=subtotal+impuestos
# print("Subtotal: ", subtotal)
# print("Taxes:", impuestos)
# print("Total",total)
print(f"""subtotal \t${subtotal:.2f}
taxes \t\t${impuestos:.2f}
total \t\t${total:.2f}""")