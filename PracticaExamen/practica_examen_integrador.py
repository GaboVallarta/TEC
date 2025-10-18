"""


"""


def inicializa_matriz():
    matriz=[
        ["RV456","Oscar Flores",45000, 5,"Ciudad del Carmen","Campeche"],
        ["DE321","Rubén Pérez",55000, 10,"Navojoa","Sonora"],
        ["AR321","Bruno López",50000, 7,"Zapopan","Jalisco"],
        ["ET453","Alan González",52000, 11,"San Juan de los Lagos", "Jalisco"],
        ["TE593","Isabel Reynoso",40000, 2,"Culiacán", "Sinaloa"],
        ["AR342","Heidy Ochoa",50000, 8,"Zapopan","Jalisco"],
        ["RS493","Fernanda Rivas",55000, 9,"Colima","Colima"]
        ]
    return matriz


# def main():
#     pass
#     f=open(r'C:\Users\adolf\Downloads\Capitulo1.txt','rt',encoding='utf-8')
#     print(f.readline())
#     print(f.readline())
#     archivo=f.readlines()
#     print(archivo)
#     #f=open('Capitulo1.txt',"r")
#     f.write(str(128.99))
#     valor=1.16
#     f.write(str(valor))
#     l=['ingreso','deposito',200,3500]
#     f.wirte(str(l))
#     f.close()

def main():
    mat=inicializa_matriz()
    salarios=0
    for i in range(len(mat)):
        salarios+=mat[i][2]
    print(salarios)
    antig=0
    for i in range(len(mat)):
        antig+=mat[i][3]
    prom=antig/len(mat)
    print(prom)
    colimenses=[]
    mayor=0
    for i in range(len(mat)):
        if mat[i][2]>mayor:
            mayor=mat[i][2]
    print(mayor)
    for i in range(len(mat)):
        if mat[i][5]=="Colima":
            colimenses.append(mat[i][1])
    print(colimenses)
main()