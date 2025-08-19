"""
These code calculates the volume of a shpere with its radius
"""

import math
radius=float(input("Enter the radius of the circle: "))
volume=(4/3)*math.pi*(math.pow(radius,3))
print(f"The volume of the sphere is: {volume:.2f} cubic units")