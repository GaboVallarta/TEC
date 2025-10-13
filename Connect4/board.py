
class Board:
    row=[]
    blank=[]
    matrix=[]
    def __init__(self,rows,cols):
        
        for j in range(rows+1):
            self.blank.append(" ")
            self.row.append([])
        for i in range(cols):
            if i==0:
                self.matrix.append(self.blank)
            self.matrix.append(self.row)
            
    def showBoard(self):
        for i in range(0,len(self.matrix),1):
            for j in range(0,len(self.row),1):
                print(self.matrix[i][j],end="")
            print()
        print()
            
    