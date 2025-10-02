"""
LISTS Quick exam.
1. Create a function that generates a list of 10 items with random numbers. Ask in the main program for
the limit for random numbers and pass it as a parameter.
2. Find out what the maximum number generated is (no need to program a function)
3. Copy the first list to another list (no function programming required)
4. Sort the second list from highest to lowest (no need to program function)
5. Create a function that receives the ordered list and sums up the items that are in the even positions
(which are in an even index).
YOUR program must be properly documented with your name and the docstrings (""", """) before
each function specifying its usefulness.
• You must handle your first function with return, the second function prints everything on itself
and not return anything.
• All variables have names that identify what they are being used for.
• Variable names are not repeated in the main program that are being used in functions.
• The call to the functions is by name. Check if it should have a return or not. And if you do,
receive it in a variable in the main program.

"""

import random


"""It generates random values and add them to the list with the append"""
def genrand(list):
    for i in range(0,10,1):
        n=random.randint(1,20)
        list.append(n)
    return list

""" Sum the elements in the even index with a for"""

def sumeven(list):
    sum=0
    for i in range(0,len(list),2):
        sum=sum+list[i]

    return sum

"""gets the list and shows the values required, also call functions such as sueven for the even number's sum"""

def show(list):
   print(list)
   maxnum=max(list)
   print("The maximum number is: ",maxnum)
   copy=list
   copy.sort()
   print("The sorted list is", copy)
   even=sumeven(list)
   print("The sum of the numbers in even positions is: ",even)
   
    
"""function main"""
def main():
    numbers=[]
    complete=genrand(numbers)
    show(complete)
    
    
    
 
    

main()

