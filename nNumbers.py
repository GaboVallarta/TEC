"""
Sum of n consecutive numbers
Write a method that receives a positive integer n, then it must compute the sum 1+2+3+...+n. Finally return the result of the sum and print it on the screen.

Input

A positive integer n

Output

The result of the sum 1+2+3...+n

Program execution example:

>>>6

21"""

n=int(input())
suma=0
for i in range(0,n,1):
    suma+=i+1

print(suma)