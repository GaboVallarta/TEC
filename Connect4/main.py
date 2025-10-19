"""Este código es para un juego de conecta 4 c
"""

from board import *
from game import *
from introducction import *



def scoreboard(save):
    with open(r"scores.csv","r") as file:
        content=file.readlines()
    print(content)
    scores=[]
    for lines in content:
        person=lines.strip().split(",")
        scores.append(person)
    
    for i in range(0,len(scores)-1):
        if save>scores[i]:
            take=scores[i]
            scores[i]=save
            save=take
            
    if len(scores)>5: 
        """falta comparar los valores realmente, el promedi con promedio, no promedio con lista xd"""
        send=scores[:5]

    with open(r"scores.csv","w") as file:
        for i in range(0,5):
            file.write(send[i])


def main():
    
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

    save=str(player_s[cont])+","+str(score)+"\n"
    
    scoreboard(save)
    

    
main()