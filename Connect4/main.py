"""Este código es para un juego de conecta 4 c
"""

from board import *
from game import *
from introducction import *

def main():
    
    board= fill_board(7,8)
    player_s=intro()
    token_s=[24,24]
    color=["x","0"]
    if len(player_s)==1:
        player_s.append("Computadora")

    print(player_s)
    end=False
    cont=0
    while(end==False):
        result=turno(player_s[cont],token_s[cont],board,color[cont])
        token_s[cont]=result[0]
        board=result[1]
        cont=(cont+1)%2
main()