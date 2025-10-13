"""
Uppercase vowels
Write a program that receives a string and outputs a new string but with all vowels in uppercase. If the word does not have vowels or the vowels are already capitalized, the output will be a String identical to the one typed by the user.

For this exercise you should NOT use the replace function of strings.

Input

A string that represents a word or phrase.

Output

A modified string taking the input string and replacing  the vowels with its uppercase vowel equivalent. If the string does not contain vowels or they are already capitalized, it returns the same string.

Program execution examples

>>> La casa azul

LA cAsA AzUl

 

>>> brtdyp

brtdyp
usaron string xd pero yo no quiero hacerlo
"""


def is_vowel(w):
    coords=[]
    vowels="aeiou"
    for i in range(len(w)):
        for i in range(len(vowels)):
            if w.find(vowels[i]):
                coords.append(w.find(vowels[i]))
    
    for i in range (len(coords)):
        w[coords[i]]=w[coords[i]].upper()       
        
    return w
word=input("hola")
print(is_vowel(word))
