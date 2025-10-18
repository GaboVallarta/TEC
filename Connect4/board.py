

def fill_board(rowsn,colsn):
    rows=[]
    matrix=[]
    for j in range(rowsn+1):
        rows.append([])
    for i in range(colsn):
        matrix.append(rows)
    return matrix
            
def showBoard(m):
    n=len(m)
    for i in range(0,n,1):
        for j in range(len(m[0])):
            print(m[i][j],end="")
        print()
    print()
            
def go_token(c,m,ficha):
    for i in range(len(m)-1):
        if m[i+1][c]!="[]" and m[i][c]==[]:
            if ficha=="x":
                m[i][c]="x"
            else:
                m[i][c]="o"
        

