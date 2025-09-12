"""
Even numbers range
Write a program that reads in the integer values a and b and displays all even numbers from a to b. Suppose a < b. If a and/or b are even, they must be included. 0 is considered even.

Input

The positive integers a and b. One in each line.

Output

The list of even numbers that are within that range (including limits). Show a number in each row.

Program execution examples

>>> 3
>>> 12                        
4
6
8
10
12
"""

a=int(input())
b=int(input())

for i in range(a,b+1,1):
    if i%2==0:
        print(i)
