"""
This program shows what discount is going to be given depending on the final purchase price and if is a frequent customer or not. 


Algorithm:
1. Ask how much of each chairs the person wants to buy and if is a frequent customer
2. Get the total price of the chairs
3. Declare a function with the parametert of the total price and if is a frequent customer
4. Use if to compare the total price and give the discount according to the price and if is a frequent customer or not
5. Display the data
"""


def check(total, C):
    discount=0
    if total>=10000 and total<20000:
        discount=10
    elif total>=20000:
        discount=15
    if C=="F":
        fdiscount=20
        print(f"As a frequent customer you get a discount of {fdiscount}% with a discount of {discount}% your total is: ${total-(total*(discount+fdiscount)/100)}")
    else:
        print(f"As a not frequent customer you get a discount of {discount}% your total is: ${total-(total*discount/100)}")
    


def chair():
    choose=input("Which type of chiar you want? basic, standart or deluxe? Use B S or D: ")
    if choose=="B":
        price=700
    elif choose=="S":
        price=900
    elif choose=="D":
        price=1500
    total=int(input("How many chairs do you want to buy?: "))
    return price*total
def main():
    client=input("Are you a frequent customer? Use F for frequent and R for not frequent: ")

    check(chair(),client)



main()