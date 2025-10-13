"""
Endpoints of a string
Design the program that receives a string and returns a string made up of the first two and last two characters of the original string.

If the length of the string it receives is less than two, it should return an empty string.

Input

A string that represents a word.

Output

Another string formed by the first and last two characters of the string received as input.

Program execution example

>>> primavera

prra

>>>uno
unno
"""
def endpoints(s):
    if len(s)<2:
        return ""
    else:
        return s[0:2]+s[-2:]

a=input("Escribe una palabra: ")
print(endpoints(a))