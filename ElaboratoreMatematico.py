from matrixHandler import *

class ElaboratoreMatematico(MatrixHandler):
    def __init__(self,  data: list[list[float]]):
        super().__init__(data)
        
    def trasponi(self):
        new_data = []
        row = 0
        column = 0
        for riga in self.data:
            pass
        return new_data
    
    def moltiplica_per_scalare(self, k:float):
        result = []
        for riga in self.data:
            new_row = []
            for elemento in riga:
                new_row.append(elemento*k)
            result.append(new_row)
                
        return result
        
#TEST
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

elaboratore = ElaboratoreMatematico(matrix)

#trasponi = elaboratore.trasponi()

scalare = elaboratore.moltiplica_per_scalare(2)

print(scalare)