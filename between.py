"""Numbers from a through b
Write a program that asks for the values a and b and displays a series of numbers from a to b. Suppose a < b.

Input

the initial value of the range (a)

the final value of the range (b)

Output

the list of values that lie between value a and value b including limits. Show the values separated by a space.

Program execution example

a value? 3
b value? 8

3 4 5 6 7 8"""

a=int(input())
b=int(input())

for i in range(a,b+1,1):
    print(i)
