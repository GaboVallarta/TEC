"""
Write a program that reads the data: base (b) and height (h) and displays the area of the triangle.

Input:

base and height, one on each row, use float values.

Output:

The area of the triangle

Program execution example
"""

height=float(input("Enter the heigh of the triangle:"))
base=float(input("Enter the base of the triangle:"))
print(f"The area of the triangle is: {(height * base) / 2} cm²")