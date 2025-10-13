"""
Mixing words
Given two strings as input, output two new words.

The two strings received as input must be split in half. If the number of characters is odd, the first half will keep the middle character. If, for example, the word has 5 characters, the first half will be left with 3 characters and the second with 2.

Two new strings will be displayed combining the halves of each received word.

Input

Two strings representing two words, each on one line.

Output

Two strings that are formed from the combination of the words received as input. The strings are each displayed on a line.

The first output word must start with the first half of the first string and end with the second half of the second string.

The second output word must start with the second half of the first string and end with the first half of the second string.

Program execution example

>>> hola

>>> amigo

hogo

laami
"""
a=input("Escribe una palabra: ")
b=input("Escribe otra palabra: ")

if len(a)%2==0:
    aa=a[0:(len(a)//2)]
    ab=a[(len(a)//2):]
else:
    aa=a[0:(len(a)//2)+1]
    ab=a[(len(a)//2)+1:]
if len(b)%2==0:
    ba=b[0:(len(b)//2)]
    bb=b[(len(b)//2):]
else:
    ba=b[0:(len(b)//2)+1]
    bb=b[(len(b)//2)+1:]

print(aa+bb)
print(ab+ba)