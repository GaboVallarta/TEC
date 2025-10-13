
f=open("answers.csv","r")
respuestas=[]
for row in f:
    print(repr(row))
    respuestas.append(row)
f.close()

lista=[]
for recorre in respuestas:
    lista.append(recorre.split(","))
print(lista)

llave=["D", "B", "D", "C", "C", "D", "A", "E", "A", "D"]

print("\tNo estudiates, No aciertos")
encabezadoEstudiantes="\tNo estudiantes \t No aciertos"
with open("resultados.csv","w") as outputFile:
    outputFile.write(encabezadoEstudiantes+"\n")
    
    for i in range(len(lista)): 
        resultados=""
        respuestas_correctas=0
        for j in range(len(lista[i])):
            if lista[i][j]==llave[j]:
                respuestas_correctas+=1
        print(f"\t\t {i+1} \t\t  {respuestas_correctas}")    
        resultados+=str(i)+","+str(respuestas_correctas)+"\n"
        outputFile.write(resultados)