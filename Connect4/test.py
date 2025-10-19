
# def scoreboard(save):
#     go=""
#     with open(r"scores.csv","r") as file:
#         content=file.readlines()
#     print(content)
#     scores=[]
    
#     for lines in content:
#         person=lines.strip().split(",")
#         print(person) #aquí
#         scores.append(person)
        
#     print(f"score's length:{len(scores)}")
#     if len(scores)<=0:
#         with open(r"scores.csv","w") as file:
#             go+=str(save[0])+","+str(save[1])+"\n"
#             file.write(go)
                
#     else:
#         for i in range(len(scores)):
#             sv=save[1]
#             print(f"sv:{sv}")
#             cs=int(scores[i][1])
#             print(f"cs:{cs}")
#             if sv>cs:
#                 take=scores[i]
#                 scores[i]=save
#                 save=take
#         print(scores)
#         with open(r"scores.csv","w") as file:
#             actualized=scores[:5]
#             for i in range(0,len(actualized)-1):
#                 go+=str(actualized[i][0])+","+str(actualized[i][1])+"\n"
#                 print("sended")
        
   
    
    

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

 

 


def main():
 
    
    score=int(input("score: "))
    name=input("name: ")
    # save=str(name)+","+str(score)
    save=[name,score]
    scoreboard(save)
    

    
main()