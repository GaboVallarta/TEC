"""
Gabriel Vallarta Ramírez

This code gives you the smalles of three integers

Algorithm:
1. Ask for the three integer
2. Declare a function which by using if compares each of the numbers
3. Return the smallest value 
4. Show the value
"""


def compare(x,y,z):
    small=x
    if small>y: # if x is smaller, it stays, if no it changes
        small=y
    if small>z: # comparing the result of the previous number, if x continue being smaller it stays, if y is smaller it stays and if no then the z takes the place
        small=z
    return small

def main():
    a=int(input("Enter the first integer: "))
    b=int(input("Enter the second integer: "))
    c=int(input("Enter the third integer: "))

   
    print(f"The smallest number between {a},{b} and {c} is: {compare(a,b,c)}")

main()