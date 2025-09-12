

"""
Countdown from b to a
Write a program that asks for the values a and b and displays a countdown of numbers going from b to a. Suppose a < b.

Input

the initial value of the range (a)

the final value of the range (b)

Output

A countdown starting at value b and ending at value a, including limits. Show the values separated by a space.

Program execution example

a value? 3
b value? 8

8 7 6 5 4 3
"""

a=int(input())
b=int(input())

for i in range(a,b-1,-1):
    print(i)
