from matrixHandler import *

class ElaboratoreMatematico(MatrixHandler):
    def __init__(self,  data: list[list[float]]):
        super().__init__(data)
        
    def trasponi(self):
        new_data = []
        row = 0
        column = 0
        for riga in self.data:
            new_data[row][column].append(riga)
            if len(self.data[row])<column:
                column += 1
        return new_data
    
    def moltiplica_per_scalare(self, k:float):
        row = 0
        column = 0
        for riga in self.data:
            for elemento in riga:
                elemento *=k
                self.data[row][column] = elemento
                column += 1
            row +=1
                
        return self.data
        
#TEST
