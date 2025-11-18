from matrixHandler import *

class ElaboratoreMatematico(MatrixHandler):
    #richiede gli stessi parametri della superclasse
    def __init__(self,  data: list[list[float]]):
        super().__init__(data)
        
    def trasponi(self):
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0

        #crea una matrice di 0 di dimensione row x column
        tmp = [[0] * rows for _ in range(cols)]

        #inverte gli elementi creando una nuova matrice
        for row in range(rows):
            for col in range(cols):
                tmp[col][row] = self.data[row][col]

        return tmp
    
    def moltiplica_per_scalare(self, k:float):
        rows = len(self.data)
        cols = len(self.data[0]) if rows > 0 else 0
        #moltiplico ogni elemento per k
        for row in range(rows):
            for col in range(cols):
                self.data[row][col] *= k
                
        return self.data
