
"""
Write a program to calculate the purchase total.

Input:

Two integers, one in each row, the first is the number of new games and the second is the number of used games.

Output:

The total of the purchase
"""
new=int(input("how many new videogames do you want to buy? "))
used=int(input("how many used videogames do you want to buy? "))

total=float(used*350+new*1000)
print(f"the total price is: ${total:.2f} pesos")