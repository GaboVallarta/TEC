import os
from board import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')





def turno(name, tokens, board,color):
    print(f"It's {name}s turn")
    print(f"Remaining tokens: {tokens}")
    showBoard(board)
    colum=int(input(f"Enter the number of the colum to put a token: "))
    
    tokens-=1
    go_token(colum,board,color)
    r=[tokens,board]
    return r

            
            

