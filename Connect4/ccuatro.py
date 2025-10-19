"""Este código es para un juego de conecta 4 c
"""

import time
import random
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def fill_board(rowsn, colsn):
    matrix = []
    for _ in range(rowsn):
        """Investigué esta forma ya que de la forma tradicional por las referencias se llenaban toda la columna de golpe, esto debido a que apuntaban al mismo espacio de memoria"""
        row = ["[ ]" for _ in range(colsn)] 
        "Se usan + en lugar de [] ya que al momento de cambiar de caracter este cambia la forma del tablero al ser de dos caracteres y el siguiente de uno solo"
        matrix.append(row)
    return matrix

            
def showBoard(m):
    n=len(m)
    for i in range(0,n,1):
        for j in range(len(m[0])):
            print(m[i][j],end="")
        print()
    print()
            

def up(board,y_pos,x_pos,ficha):
    cont=1
    if y_pos<3:
        return cont
    if y_pos-3>=0:
        for i in range(1,4):
            if board[y_pos-i][x_pos]==ficha:
                cont+=1
            else:
                return cont
    return cont

def down(board,y_pos,x_pos,ficha): 
    cont=1
    if y_pos+3>= len(board):
        return cont
    
    if y_pos+3<=len(board)-1:
        for i in range(1,4):
            if board[y_pos+i][x_pos]==ficha:
                cont+=1
            else:
                return cont
    return cont

def left(board,y_pos,x_pos, ficha):
    cont=1
    if x_pos<3:
        return cont
    if x_pos-3>=0:
        for i in range(1,4):
            if board[y_pos][x_pos-i]==ficha:
                cont+=1
            else:
                return cont
    return cont

def right(board,y_pos,x_pos, ficha):
    cont=1
    if x_pos+3>=len(board[0]):
        return cont
    if x_pos+3<=len(board[0])-1:
        for i in range(1,4):
            if board[y_pos][x_pos+i]==ficha:
                cont+=1
            else:
                return cont
    return cont

def check(board,y_pos,x_pos,ficha):
    c=False
    if(up(board,y_pos,x_pos,ficha)+down(board,y_pos,x_pos,ficha) >3 or left(board,y_pos,x_pos,ficha)+right(board,y_pos,x_pos,ficha)>3 or diag_di(board,y_pos,x_pos,ficha)>3 or diag_id(board,y_pos,x_pos,ficha)>3):
        c=True
    return c
    """aquí hay break, no sé si se pueda usar no recuredo la verdad"""
def diag_id(board, y_pos, x_pos, ficha):
    cont = 1
   
    for i in range(1, 4):
        if y_pos + i < len(board) and x_pos + i < len(board[0]) and board[y_pos + i][x_pos + i] == ficha:
            cont += 1
        else:
            break
    
    for i in range(1, 4):
        if y_pos - i >= 0 and x_pos - i >= 0 and board[y_pos - i][x_pos - i] == ficha:
            cont += 1
        else:
            break
    return cont

def diag_di(board, y_pos, x_pos, ficha):
    cont = 1
    
    for i in range(1, 4):
        if y_pos + i < len(board) and x_pos - i >= 0 and board[y_pos + i][x_pos - i] == ficha:
            cont += 1
        else:
            break
    for i in range(1, 4):
        if y_pos - i >= 0 and x_pos + i < len(board[0]) and board[y_pos - i][x_pos + i] == ficha:
            cont += 1
        else:
            break
    return cont



def go_token(c,m,ficha):
    put=False
    end=False
    i=len(m)-1
    while i>=0 and put==False:
        if m[i][c]=="[ ]":#este if es necesario?
            if ficha=="[x]":
                m[i][c]="[x]" 
                end=check(m,i,c,"[x]")
            else:
                m[i][c]="[o]"
                end=check(m,i,c,"[o]")
            
            put=True
        else:
            i-=1
    return end





def turno(name, tokens, board,color):
    print(f"It's {name}'s turn")
    print(f"Remaining tokens: {tokens}")
    showBoard(board)
    finish=False
    
    tokens-=1
    correct=True
    while(correct):

        if not name== "Computadora":
            colum=(input(f"Enter the number of the colum to put a token: "))
        else:
            colum=random.randint(1,7)
            print(f"Computre choosed: {colum}")
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
    r=[tokens,board,finish]
    return r

            
            



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
        print("Are you gonna play with a friend?")
        

        x=input("1. Yes\n2. No\n")
        if x.isdigit():
            x=int(x)
            if(x==1 or x==2):
                choice=x
                segundo=False
            else:
                print("Invalid option, try again")
                time.sleep(1)
                cls()
        else:
            print("Invalid option, try again")
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
    elif c==2:
        pass
    else:
        print(" Invalid answere, you are going to play with one player")
        time.sleep(2)
    return players




def main():
    
    board= fill_board(6,7)
    player_s=intro()
    token_s=[24,24]
    color=["[x]","[0]"]
    if len(player_s)==1:
        player_s.append("Computadora")
    """a veces no pone el jugador del turno que sigue, solo el primero, por eso no quité el print, no se qué pasa XD"""
    print(player_s)
    end=False
    cont=0
    while(end==False):
        result=turno(player_s[cont],token_s[cont],board,color[cont])
        token_s[cont]=result[0]
        board=result[1]
        end=result[2]
        if end==False:cont=(cont+1)%2
    showBoard(board)
    print(f"{player_s[cont]} ha ganado")
main()