from matrixHandler import *

class ElaboratoreMatematico(MatrixHandler):
    #richiede gli stessi parametri della superclasse
    def __init__(self,  data: list[list[float]]):
        super().__init__(data)
        
    def trasponi(self):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        tmp = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                tmp[col][row] = matrix[row][col]

        return tmp
    
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
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11]
]

elaboratore = ElaboratoreMatematico(matrix)

trasponi = elaboratore.trasponi()
matrix_trasponi = MatrixHandler(trasponi)

matrix_trasponi.print_matrix()