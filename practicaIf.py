"""Gabriel Vallarta Ramírez
Pseudocode

Pseudocode:
1. Ask how many boxes of warm, energy saving and circular light bulbs the user wants to buy.
2. Chech the price of each box 
3. Calculate the total price of each type of box 
4. Calculate the total price of the purchase
5. If it is less than 5000 pesos, then there is a single exhibition
6. If it is between 5000 and 30000 pesos, he has 3 months without interests
7. If it is more than 30000 pesos, the user can choose between a single exhibition with 5% of discount or 9 months without interest

"""

#separador de miles es la coma


print(f"This program calculates the total price of your purchase of light bulbs and gives you different payment options according on the total price")

warm=int(input("How many boxes of warm light bulbs do you want to buy?: "))
saving=int(input("How many boxes of energy saving light bulbs do you want to buy?: "))
circular=int(input("How many boxes of circular light bulbs do you want to buy?: "))

if warm<0 or saving<0 or circular<0:
    print("One or more input is less than 0")
    warm=0
    saving=0   
    circular=0


total=warm*250+saving*700+circular*1000

print(f"The total price of your purchase is: ${total:.2f} pesos")

if total<=0:
    print("There is no purchase")
elif total<5000:
    print("You have to pay in a single exhibition")
elif total<=30000:
    total=float(total/3)
    print(f"You can pay in 3 months without interests in payments of {total:,.2f} pesos")
else:
    choose=int(input(f"""Because your purchase was more than 30000 pesos you can choose between:
                 
     1. single exhibition with a discount of 5%
     2. 9 months without interests
                 
    Type your choice: """))
    
    if choose==1:
        print(f"You have chosen a single exhibition of {total*0.95:,.2f} pesos")
    elif choose==2:
        
        print(f"You have chosen 9 months without interests, the payments will be of {total/9:,.2f} pesos") #la coma es separador de miles
    else:
        print("Invalid option")