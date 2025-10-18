"""no funciona ya que el kb está en el fi, por lo que tiene que esperar cada 1.5 segundos a que se presione enter"""
from game import cls

import time
import sys


def name(x):
    print("What's your name?")
    name=input(f"Player {x}: ")
    return name


def one_or_two():
    time.sleep(0.3)
    segundo=True
    choice=1
    while(segundo):
        cls()
       
        key=""
        print("Are you gonna play alone or with a friend?")
        

        x=int(input("1. Yes\n2. No\n"))
        if(x==1 or x==2):
            choice=x
            segundo=False
        else:
            print("Invalid option, try again")
            time.sleep(1)
            cls()
    return choice

def introduction():
    print("Welcome to Connect 4")
    print("The objective of the game is to connect 4 tokens in a row, either horizontally, vertically, or diagonally.")
    print("Players take turns dropping their tokens into one of the columns on the board.")
    print("The first player to connect 4 tokens wins!")
    print("If the board fills up and no player has connected 4 tokens, the game ends in a draw.")
    print("Enjoy the game!")
    print("Press enter to continue")
    x=input()


def intro():
    introduction()
    players=[]
 
    cls()
    x=1
    name_one=name(x)
    players.append(name_one)
    c=one_or_two()
    if c==1:
        x=2
        name_two=name(x)
        players.append(name_two)
    return players
