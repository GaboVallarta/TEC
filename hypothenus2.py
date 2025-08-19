"""
These code calculates the hypothenuse with the opposite side and the angle

Pseudocode:
1. Import math
2. Ask the user for the angle in degrees and the length of the opposite side
3. Calculate the hypothenuse using the formula: hypothenuse = opposite / sin(angle in radians) with the funciton sin and radians from math
4. Print the result

"""

import math

angle=float(input("Enter the angle in degrees: "))
opposite=float(input("Enter the length of the opposite side: "))

hypothenus= opposite/math.sin(math.radians(angle))

print(f"The length of the hypothenus is: {hypothenus:.2f} units")