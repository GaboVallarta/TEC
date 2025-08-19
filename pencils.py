"""
This program calculates how much boxes of pencils are able to be done with a given number of pencils.

Pseudocode:

1. Get the number of pencils
2. Divide the number by 200 for the big boxes, and save the remaining pencils with modululs, repeat with the medium and small boxes
3. Print the result of boxes and remaining pencils

"""

pencils = int(input("Enter the number of pencils you have: "))

bigbox= pencils // 200
remaining = pencils % 200
mediabox= remaining // 50
remaining = remaining % 50
smallbox = remaining // 10
remaining = remaining % 10

print(f"You can make {bigbox} big boxes, {mediabox} medium boxes, and {smallbox} small boxes with {remaining} pencil(s) remaining.")