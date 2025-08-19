"""
Gabriel Vallarta
This program calculates the age of the user in 2037
Algorithm:
---------------
1.Write what this program stands for
2. We must ask the user for ther/his year of birth
3. Substract 2037 minus year of birth to find out the age in 2037
4. Inform the user abut her/His future age
-----------------
Pseudocode:
---------------------
1.Print("this program calculates your age in 2037")
2. Print("Tell me your birth year:")
3.year_birth = input()
4.age_2037= 2037 - year_birth
5. Print("Your age in 2037 year is going to be: ", age_2037, "years old")
"""

print("this program calculates your age in 2037")
name=input("What is your name? ")
year_birth = int(input("Tell me your birth year:"))
age_2037=2037-year_birth
print(name+" your age in 2037 year is going to be: ", age_2037, "years old")