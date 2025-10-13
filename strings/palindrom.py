"""
Palindrome
Write a program that contains a function to identify if a given string is a palindrome or it is not.

"A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar.." (https://en.wikipedia.org/wiki/Palindrome).

The program should work even if the input string includes spaces between words and if there are letters uppercase or lowercase.

Input

A string that represents a word or phrase, which we want to know if it is a palindrome or not.

Output

A message indicating whether or not it is a palindrome with the following format: "It is a palindrome" or "It is NOT a palindrome".

Program execution example

>>> Anita lava la tina

It is a palindrome

 

>>> La casa Azul

It is NOT a palindrome

 
 """

def is_palindrome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]

a=input("Escribe una palabra o frase: ")
if is_palindrome(a):
    print("It is a palindrome")
else:
    print("It is NOT a palindrome")