from MatrixHandler import *

def moltiplica_matrice(matrix_1:MatrixHandler, matrix_2:MatrixHandler):
    row_matrix_1 = len(matrix_1)
    column_matrix_1 = len(matrix_1[0])
    column_matrix_2 = len(matrix_2[0])
    
    #matrice di 0 con le colonne della matrice 1 e le righe della matrice 2
    tmp = [[0] * column_matrix_2 for _ in range(row_matrix_1)]
    
    for i in range(row_matrix_1):
        for n in range(column_matrix_2):
            for k in range(column_matrix_1):
                tmp[i][k] += matrix_1[i][k] * matrix_2[k][n]
                
    return tmp