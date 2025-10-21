"""Este código es para un juego de conecta 4 c
"""

import os
import random
import time

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
    if((up(board,y_pos,x_pos,ficha)+down(board,y_pos,x_pos,ficha))-1>3 or (left(board,y_pos,x_pos,ficha)+right(board,y_pos,x_pos,ficha)-1)>3 or (diag_di(board,y_pos,x_pos,ficha)-1)>3 or (diag_id(board,y_pos,x_pos,ficha)-1)>3):
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

def remove_token(board, color):
    removed = False
    removed_color = "[]"
    removed_col = 0
    removed_rows = []

    while not removed:
        try: # la funcion try except para evitar que el usuario meta letras u otros caracteres
            col = int(input("Enter the column number of the token you want to remove: ")) - 1
            row = int(input("Enter the row number of the token you want to remove (top=1, bottom=6): ")) - 1
        except ValueError:
            print("Invalid input. Use numbers only.")
            continue

        # check if the chosen position is inside the board
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            print("That position is outside the board.")
            continue # continue the loop to ask for input again

        # check if the chosen space belongs to the other player, wouldn't make sense to remove your own token
        if board[row][col] != "[ ]" and board[row][col] != color:
            removed_color = board[row][col]
            removed_col = col
            print(f"You removed {removed_color} at row {row+1}, column {col+1}!")
            board[row][col] = "[ ]"
            removed = True
        else:
            print("You can only remove the other player's token.")

    # Colapsar la columna tras quitar la ficha
    collapse_column(board, col)

    # Revisar toda la columna afectada para ver si alguien ganó
    win = False
    win, winner_color = check_victory_after_removal(board)
    return board, win, winner_color

def collapse_column(board, col):
    removed_rows = []

    for row in range(len(board)-1, -1, -1):
        if board[row][col] == "[ ]":
            # find the nearest token above
            for above_row in range(row-1, -1, -1):
                if board[above_row][col] != "[ ]":
                    # move the token down
                    board[row][col] = board[above_row][col]
                    board[above_row][col] = "[ ]"
                    break

def check_victory_after_removal(board):
    """
    Revisa todo el tablero después de quitar un token
    para detectar si alguien tiene Connect 4.
    """
    for r in range(len(board)):
        for c in range(len(board[0])):
            ficha = board[r][c]
            if ficha != "[ ]":  # solo revisar si hay ficha
                if check(board, r, c, ficha):
                    return True, ficha  # devuelve True y el color ganador
    return False, None


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def turno(name, tokens, board,color,bullet_mode,bullet_time):
    print(f"It's {name}'s turn")
    print(f"Remaining tokens: {tokens}")
    showBoard(board)
    finish=False
    
    tokens-=1
    correct=True
    start=0
    end=0
    if bullet_mode and name != "Computadora":
        start_bullet = time.time()
        remaining_tinme = bullet_time
    else:
        start=time.time()

    while(correct):

        # PLAYER
        if name != "Computadora":
            print("Do you want to (1) place a token or (2) remove an opponent's token?")
            choice = input("Choose 1 or 2: ")

            if choice == "2":
                board, finish, winner_color = remove_token(board, color)
                correct = False
                t = 0
                r = [tokens, board, finish, t]
                return r
            else:
                colum = input("Enter the number of the column to put a token: ")
        
        else:
            # COMPUTER

            decision = random.choice(["place", "remove"])
            if decision == "remove":
                # find valid token to remove
                valid_positions = []
                for r in range(len(board)):
                    for c in range(len(board[0])):
                        if board[r][c] != "[ ]" and board[r][c] != "[o]":  # check if the column isn't empty and the token is the player's
                            valid_positions.append((r, c))

                if valid_positions:
                    row, col = random.choice(valid_positions)
                    print(f"Computer removes a token from column {col + 1}, row {row + 1}")

                    # Remove the token manually and collapse column
                    board[row][col] = "[ ]"
                    collapse_column(board, col)

                    # Check if anyone won after removal
                    finish, winner_color = check_victory_after_removal(board)
                    correct = False
                    t = 0
                    r = [tokens, board, finish, t]
                    return r
                else:
                    print("Computer couldn't find a token to remove.")
                    decision = "place"  # since it can't remove, it will place
            
            if decision == "place":
                colum=random.randint(1,7)
                print(f"Computer chose: {colum}")
                colum=str(colum)
                """lo hago string para que tenga la función de is digit, más que nada para evitar hacer más condiciones"""
                time.sleep(2)

        if colum.isdigit():
            
            colum=int(colum)
            colum-=1
            if colum<len(board[0]) and colum>=0 and board[0][colum]=="[ ]":
                finish=go_token(colum,board,color)
                correct=False
            else:
                print("Invalid answer, try again.")
        else:
            print("Invalid answer, try again.")
    end=time.time()

    t=end-start
    r=[tokens,board,finish,t]
    
    return r


"""no funciona ya que el kb está en el fi, por lo que tiene que esperar cada 1.5 segundos a que se presione enter"""
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
                print("Invalid option, try again.")
                time.sleep(1)
                cls()
        else:
            print("Invalid option, try again.")
            time.sleep(1)
            cls()

       
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
        print("Invalid answer, you are going to play with one player.")
        time.sleep(2)
    return players


def scoreboard(save):
    # Leer archivo
    scores = []
    with open("scores.csv", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                scores.append([parts[0], float(parts[1])])

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
        
    enter=input("Press enter to continue")
    cls()


def bullet():
    bullet=False
    go=True
    print(f"""Do you wanna play bullet mode?
1.Yes
2.No
""")
    e=input()
    while(go):
        if e.isdigit():
            e=int(e)
            if e==1:
                bullet=True
                go=False
            elif e==2:
                go=False
            else:
                print("Invalid option, try again.")
                time.sleep(1)
                cls()    
        else:
            print("Invalid option, try again.")
            time.sleep(1)
            cls()
    return bullet
 
def play():
    
    board= fill_board(6,7)
    player_s=intro()
    tygame=bullet()
    token_s=[24,24]
    times=[0,0]
    color=["[x]","[0]"]
    if len(player_s)==1:
        player_s.append("Computadora")
    """a veces no pone el jugador del turno que sigue, solo el primero, por eso no quité el print, no se qué pasa XD"""
    print(player_s)
    end=False
    cont=0
    winner_index = 0
    
    while(end==False):
        result=turno(player_s[cont],token_s[cont],board,color[cont],tygame,bullet_time=10)
        token_s[cont]=result[0]
        board=result[1]
        end=result[2]
        times[cont]+=result[3]
        if end==False:
            cont=(cont+1)%2
        else:
            winner_index = cont

    showBoard(board)
    print(f"{player_s[winner_index]} has won with a time of {times[winner_index]:.2f} seconds.")
    
    score=(24-token_s[cont])/times[cont]

    save=[player_s[cont],score]
    
    scoreboard(save)
    

    
def main():
    game=True
    while(game):
        print(f"""Welcome to Connect 4, what do you want to do?
1.Play
2.Check scoreboard
3.Exit
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
                print("Invalid option, try again.")
                time.sleep(1)
                cls()
        else:
            print("Invalid option, try again.")
            time.sleep(1)
            cls()



main()