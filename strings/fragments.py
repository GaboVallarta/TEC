"""
String fragments
Write a program that reads a string and displays fragments of it.

Input

A string.

Output

In the first line print the length of the received string.

In the second line print only the first character of the received string.

In the third line print only the last character of the received string.

In the fourth line print only the characters with odd index inside the string.

Program execution example

>> Texto

5

T

o

et
"""

a=input("Escribe una palabra: ")
print(len(a))
print(a[0])
print(a[-1])
print(a[1::2])