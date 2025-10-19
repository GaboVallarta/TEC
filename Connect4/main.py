"""Este código es para un juego de conecta 4 c
"""

from board import *
from game import *
from introducction import *


def scoreboard(save):
    # Leer archivo
    scores = []
    with open("scores.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                scores.append([parts[0], int(parts[1])])

    # Insertar nuevo score en orden descendente
    inserted = False
    for i in range(len(scores)):
        if save[1] > scores[i][1]:
            scores.insert(i, save)
            inserted = True
            break
    if not inserted:
        scores.append(save)

    # Mantener solo los 5 mejores
    scores = scores[:5]

    # Reescribir todo el archivo
    with open("scores.csv", "w") as file:
        for person in scores:
            file.write(f"{person[0]},{person[1]}\n")
            print(f"Wrote: {person[0]},{person[1]}")

def show_score():
    score=[]
    with open("scores.csv","r") as file:
        
        for person in file:
            lista=person.strip().split(",")
            score.append(lista)
    print(f"Names:\t\tScore:")
    for i in range(len(score)):
        for j in range(len(score[0])):
            print(score[i][j], end="\t\t")
        print()
        
    enter=input("press enter to continue")
    cls()



 
def play():
    
    board= fill_board(6,7)
    player_s=intro()
    
    token_s=[24,24]
    times=[0,0]
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
        times[cont]+=result[3]
        if end==False:cont=(cont+1)%2
    showBoard(board)
    print(f"{player_s[cont]} ha ganado con un tiempo de {times[cont]:.2f} segundos")
    
    score=(24-token_s[cont])/times[cont]

    save=[player_s[cont],score]
    
    scoreboard(save)
    

    
def main():
    game=True
    while(game):
        print(f"""Welcome to connect 4, what do you want to do?
1.Play
2.Check scoreboard
3.exit
          """)
        choose=input()
        if choose.isdigit():
            choose=int(choose)
            if choose==1:
                play()
            elif choose==2:
                cls()
                show_score()
            elif choose==3:
                game=False
            else:
                print("Invalid option, try again")
                time.sleep(1)
                cls()
        else:
            print("Invalid option, try again")
            time.sleep(1)
            cls()



main()