"""
These code gets the area of a triangle with the lengths of its sides.
"""

import math

a=float(input("Enter the first lenght: "))
b=float(input("Enter the second lenght: "))
c=float(input("Enter the third lenght: "))


s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"The area of the triangle is: {area:.2f} square units")