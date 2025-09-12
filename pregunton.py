"""
These program is a survey about my favorite topics

Pseudocode:
1. Show the first question
2. Input the answer and check if it is the correct one 
3. If it is correct go to the next question, if not end the program

"""

print("Welcome to the survey about my favorite topics")

print(f"""Which video game from Fromsoftware won a GOTY?
      1. Elden Ring
      2. Dark Souls
      3. Sekiro""")
answere=int(input("choose your number: "))

if answere==3:
    print("Well done, you advance to the next step")

    print(f"""Which is the most sold videogame
      1. Fortnite
      2. Tetris
      3. Roblox""")
    answere=int(input("choose your number: "))

    if answere==2:
        print("Well done, you advance to the final step")
        print(f"""Which game lasted less than a week in the store
        1. Concord
        2. Age of empire
        3. Batman Arkam Knight""")
        answere=int(input("choose your number: "))
        if answere==1:
            print("You WON")
        else:
            print("you lose")
    else:
        print("You lose")
        exit()



else:
    print("you lose")
    exit()