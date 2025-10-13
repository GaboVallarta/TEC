import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')



class Game:
    player1=None
    player2=None   
    board=None
    

    def __init__(self,player1,player2,board):
        self.player1=player1
        self.player2=player2
        self.board=board
        self.board[0][0]="V"
    
    def turno(self,player):
        next=False
        while not next:
            print(f"Es el turno de{player.name}")
            print(f"Fichas restantes: {player.token}")
            

