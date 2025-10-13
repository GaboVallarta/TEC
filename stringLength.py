"""
String length
Create a program that prompts the user for two character strings as input and prints the longest string to the console. If the two strings are the same length, the function should print both strings one on each line.

Input

Two strings, each on one line.

Output

The longest string or both if they have the same length

Program execution example

>>> Guanajuato

>>> Jalisco

Guanajuato

 

>>> dog

>>> cat

dog

cat

 """

a=input("Escribe una palabra: ")
b=input("Escribe otra palabra: ")

if len(a)>len(b):
    print(a)
elif len(b)>len(a):
    print(b)
else:
    print(a)
    print(b)