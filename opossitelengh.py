"""
These code gives the lenght of the opposite side with the hypothenus of a triangle
 

Pseudocode:
1. Tell the user about the program
2. Angle=30
3.Asl the value of the hypothenuse
4.Convert the anglo to radians
5.Use the formula 
oppositeside=angle*hypothenus
6.Print the result
"""

import math
hypothenus=float(input("Enter the length of the hypothenus: "))
angle=math.sin(math.radians(30))  

oppossite=angle*hypothenus

print(f"The length of the opposite side is: {oppossite:.2f} units")