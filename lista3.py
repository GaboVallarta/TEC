
lista=[]
n=0
odd=0
even=0
go=True
while go==True:
    n=int(input("Ingrese un valor: "))
    if n<0:
        go=False
    else:
        lista.append(n)

for i in range(0,len(lista),1):
    if lista[i]%2==0:
        even+=1
    else:
        odd+=1
print("Odd:",odd)
print("Even:",even)

    
        
    