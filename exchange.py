"""
These code changes from pesos to dollars

Pseudocode:
1. Ask the user for the amount of pesos they want to change.
2. Ask the user for the cost of the dollar in pesos.
3. Convert the amount of pesos to dollars by divinding the pesos by the cost of the dollar
4. Print the result in dollars.

"""

#ask the user for the amount of pesos and the cost of the dollar
quantity=float(input("How much pesos do you want to change?: "))
dollarcost=float(input("How much does the dollar costs? : "))

#convert pesos to dollars by dividing the quantity by the cost of the dollar
dollars=quantity/dollarcost


#print the result
print(f"you have {dollars:.2f} dollars")