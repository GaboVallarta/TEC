"""
Write a program that adds the integers (positive and negative) that the user types and stops until the user types a zero.

Input

A sequence of positive or negative integers. The sequence must end with a 0.

Output

The sum of the numbers typed.

Program execution example:

>>>2
>>>5
>>>6
>>>0

13
"""




# def main(): esto dicen que esta mal, lo del while true
#     suma=0
#     while True:
#         i=int(input())
#         suma+=i
#         if i==0:
#             break
#     print(suma)

# main()


suma=0
num=int(input())
while num !=0:
        suma+=num
        num=int(input())
print(suma)