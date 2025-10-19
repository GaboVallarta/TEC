import os
from board import *
import random
import time
def cls():
    os.system('cls' if os.name=='nt' else 'clear')





def turno(name, tokens, board,color):
    print(f"It's {name}'s turn")
    print(f"Remaining tokens: {tokens}")
    showBoard(board)
    finish=False
    
    tokens-=1
    correct=True
    start=0
    end=0
    while(correct):

        if not name== "Computadora":
            start=time.time()
            colum=(input(f"Enter the number of the colum to put a token: "))
            
        else:
            colum=random.randint(1,7)
            print(f"Computre choosed: {colum}")
            colum=str(colum)
            """lo hago string para que tenga la función de is digit, más que nada para evitar hacer más condiciones"""
            time.sleep(2)
        if colum.isdigit():
            
            colum=int(colum)
            colum-=1
            if colum<len(board[0]) and colum>=0:
                finish=go_token(colum,board,color)
                correct=False
            else:
                print("invalid answere, try again")
        else:
            print("invalid answere, try again")
    end=time.time()
    t=end-start
    r=[tokens,board,finish,t]
    
    return r

            
            

