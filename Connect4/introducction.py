"""no funciona ya que el kb está en el fi, por lo que tiene que esperar cada 1.5 segundos a que se presione enter"""
from game import clear
import keyboard as kb
import time
import sys
def intro():
    players=[]
    enter=True
    print("Welcome to Connect 4")
    print("The objective of the game is to connect 4 tokens in a row, either horizontally, vertically, or diagonally.")
    print("Players take turns dropping their tokens into one of the columns on the board.")
    print("The first player to connect 4 tokens wins!")
    print("If the board fills up and no player has connected 4 tokens, the game ends in a draw.")
    print("Enjoy the game!")
    print("Press Enter to continue")

    while enter:
        if kb.is_pressed('enter'):
            enter=False
        # else:
        #     for c in ["   ",".  ",".. ","..."]:#"""std out es el flujo de salida estándar de texto, es decir, la pantalla"""
        #         sys.stdout.write('\r'+c) 
        #         sys.stdout.flush()
        #         time.sleep(0.5)
    enter=True
    clear()
    time.sleep(1)
    print("What is your name?")
    
    name=input("Player 1: ")
    # while(enter):
        # if kb.is_pressed('enter'):
        #     enter=False
        
    
    print("Are you gonna play alone or with a friend?")