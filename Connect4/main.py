"""Este código es para un juego de conecta 4 con pygame como librería de gráficos
"""

from board import Board as Bd
from game import *
from introducction import *

def main():
    intro()
    board=Bd(7,8)
    board.showBoard()

    

main()