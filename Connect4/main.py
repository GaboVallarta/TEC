"""Este código es para un juego de conecta 4 c
"""

from board import *
from game import *
from introducction import *

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