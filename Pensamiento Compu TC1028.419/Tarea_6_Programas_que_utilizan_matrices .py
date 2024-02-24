# -*- coding: utf-8 -*-
"""
Date: 30 of september 2022
Course: Pensamiento computacional para ingeniería (Gpo 419)
    
Assingment: Tarea 6: Programas que utilizan matrices (listas de listas)

Gabriel Melendez - A01638293
"""
def inputs():
    matrix = []
    print('>>> New Matrix')
    while True:
        row_values = input('>>> ')
        if row_values == '':
            return matrix
        matrix.append(row_values.split())    
        
def matrix_sums(matrix_1,matrix_2):
    sum_of_matrices = []
    for index, (row_1, row_2) in enumerate(zip(matrix_1,matrix_2)):
        sum_of_matrices.append([])
        print(index)
        for x,y in zip(row_1,row_2):
            sum_of_matrices[index].append(int(x) + int(y))
    return sum_of_matrices

def main():
    matrix_1 = inputs()
    matrix_2 = inputs()
    print(matrix_1,matrix_2)
    matrix_3 = matrix_sums(matrix_1, matrix_2)
    for x,y in zip(matrix_1,matrix_2):
        if len(x) != len(y) or len(matrix_1) != len(matrix_2):
            matrix_3 = 'Las matrices no son del mismo tamaño'
            break
    
    print(matrix_3)
    return

main()