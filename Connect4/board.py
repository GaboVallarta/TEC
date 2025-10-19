

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


