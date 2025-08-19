"""
These code calculates the volume of a tetrahedron with its arist length

Pseudocode:
1. Import math
2. Ask the user for the length of the arist
3. Calculate the volume using the formula: volume = pow(a,2)*sqrt(3) with the function sqrt from math
4. Print the result
"""

import math
a=float(input("Enter the length of the arist: "))
volume=math.pow(a,3)*math.sqrt(3)
print(f"The volume of the tetrahedron is: {volume:.2f} cubic units")