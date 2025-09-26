


"""

Adhering to the Code of Ethics for Students of Tecnológico de Monterrey, I promise that my performance in this
exam will be governed by academic honesty. In accordance with the commitment made when signing said code,
I will take this exam honestly and personally, to reflect, through it, my knowledge and subsequently accept the
evaluation obtained.
Name:Gabriel Vallarta Ramírez                   Career: ITC             Group:404


"""


def adding_price(subtotal,price):#This function adds the new price to the total
    total=subtotal+price
    return total

def reward(subtotal): # This function checks if the person gets points
    points=0
    if(subtotal>=200):
        points=20
    elif(subtotal>=100):
        points=10
    elif(subtotal>=50):
        points=5
    else:
        points=0
    return points

def main():
    finish_order=False
    total=0.00
    products=0
    while finish_order==False:
        print(f"""
---Welcome to Coffe World!---
      
1.Hot chocolate $35.50
2.Vanilla latte     $50.00
3.Chai latte  $70.00
4.Sandwitch    $20.00
5.Finalize order
-------------------------------
""")
        choose=int(input("Enter your option order: "))
        if choose==5:
            finish_order=True
        elif choose==1:
            total=adding_price(total,35.50)
            products+=1
        elif choose==2:
            total=adding_price(total,50.00)
            products+=1
        elif choose==3:
            total=adding_price(total,70.00)
            products+=1
        elif choose==4:
            total=adding_price(total,20.00)
            products+=1
        else:
            print(f"Please enter a valid number :)")
    print(f"The total price is {total:,.2f} pesos, with a total of {products} items",end=" ")
    points=reward(total)
    if(points!=0):
        print(f"and because of the total price, you accumulate {points} points")
    else:
        print(f"and because of the total price was lower than 50, you have no accumulated points")
        

main()