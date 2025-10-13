"""
Reverse String
Write a program that reads a string and outputs the received string written in reverse, starting with the last character and ending with the first character of the original string, and all uppercase.

Input

a string

Output

The entered string, but backwards and in uppercase.

Program execution example

>>> Texto

OTXET
"""
a=input("Escribe una palabra: ")
print(a[::-1].upper())