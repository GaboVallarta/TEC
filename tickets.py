"""
These code calculates the exchange for a little girl 

Pseudocode:
1. Ask the user for the amount of money
2. Divide by 200 and use modulus to get the remains, repeat with 50 and 20
3. Print the results with unites


"""

coins=int(input("Enter the amount of money you have: "))
billstwo= coins // 200
remaining= coins % 200
billsfive= remaining // 50
remaining= remaining % 50
billstwen= remaining // 20
remaining= remaining % 20

print(f"You have {billstwo} 200-unit bills, {billsfive} 50-unit bills, {billstwen} 20-unit bills and {remaining} remaining coins.")