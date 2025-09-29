list=[]
inverted=[]
n=0
while n!=-1:
    n=int(input("Ingrese un valor: "))
    if n!=-1:
        list.append(n)

for i in range(len(list)-1,-1,-1):
    inverted.append(list[i])

print(list)
print(inverted)