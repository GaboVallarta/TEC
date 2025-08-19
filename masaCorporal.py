"""
These code calculates your body mass index with your weight and height.

Pseudocode:
1. Ask the user for their weight in kilograms  and his height in meters
2. Get the IMC by dividing the weight by the height to the power of two
3. Print the result 


"""

#ask the user for their weight and height
weight=float(input("Register your weight in kg: "))
height=float(input("Register your height in meters: "))

#calculate the body mass index by dividing the weight by the square of the height
IMC=weight/(height**2)
 #print the result
print(f"Your IMC is: {IMC:.2f}")