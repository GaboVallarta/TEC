"""
These program calculates the hypothenuse with the given cathetus.

Pseudocode:
1. Import math
2. Ask for both cathetus
3. Use function hypot from math 
4. Print the result


"""
import math
catone=float(input("Enter the length of the first cathetus: "))
cattwo=float(input("Enter the length of the second cathetus: "))

hypothenuse=math.hypot(catone, cattwo)

print(f"The length of the hypothenuse is: {hypothenuse:.2f} units")