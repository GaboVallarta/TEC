"""
Gabriel Vallarta
This program calculates the total prices of items with taxes

"""


cant_articulos=int(input()) #Number of items
precio=float(input())# Total price 
subtotal=cant_articulos*precio# Subtotal
impuestos=subtotal*0.16#Taxes calculation
total=subtotal+impuestos#Total calculation with prices and taxes
print(subtotal)# Subtotal
print(impuestos)# Taxes
print(total)# Total price with taxes