"""
These code calculates the are of a circle with its radius.

Pseudocode:
1. Import math
2. Ask the user for the radius of the circle
3. Calculate the area using the formula: area = π * radius²
4. Print the result

"""

import math
radius = float(input("What is the lenght of the radius?: "))
area = math.pi * (radius ** 2)

print(f"The area of the circle is: {area:.2f} square units")