# -*- coding: utf-8 -*-
"""
Date:
Course:
    
Assingment:

Gabriel Melendez - A01638293
"""
from random import randint
list_of_Prime_numbers = ['02 ','03 ','05 ','07 ','11 ','13 ','17 ','19 ','23 ','29 ','31 ','37 ','41 ','43 ','47 ','53 ','59 ','61 ','67 ','71 ','73 ','79 ','83 ','89 ','97 ','101','103','107','109','113','127','131','137','139','149','151','157','163','167','173','179','181','191','193','197','199']

def gamemode(difficulty='Easy'):
    if difficulty == 'Hard' or difficulty == 'hard' or difficulty == 'h':
        size_Col, size_Row, num_mines = 24, 20, 99
    elif difficulty == 'Medium' or difficulty == 'medium' or difficulty == 'm':
        size_Col, size_Row, num_mines = 18, 15, 40
    elif difficulty == 'Easy' or difficulty == 'easy' or difficulty == 'e' or difficulty == '':
        size_Col, size_Row, num_mines = 10, 8, 10
    else:
        return 
    return size_Col, size_Row, num_mines

#This function creates a matrix of lists according to column and row sizes given
def listoflists_maker(col, row, val=0):
    main_matrix = []
    for i in range (row):
        main_matrix.append([])
        for n in range (col):
            main_matrix[i].append(val)
    return main_matrix

# This function takes a list of lists & Inserts n-number of x's at random coordinates from the list of lists
def assign_mines(lists, num_mines): 
    counter = 0
    while counter != (num_mines): 
        row = randint(0,(len(lists)-1))
        col = randint(0,(len(lists[0])-1))
        if lists[row][col] != 'X':
           lists[row][col] = 'X'
        else:
           counter -= 1   
        counter += 1
    return lists

# This adds 0's to the outside of the list to facilitate the indexing process
def prep_matrix(matrix): 
    
    for index, row_vals in enumerate(matrix):
        matrix[index][:0] = ['N']
        matrix[index].append('N')
    matrix[:0] = [['N']*(len(row_vals))]
    matrix.append((['N']*(len(row_vals))))
    return matrix

# This function reverts what assign_tiles() does but keeps the values it modified
def regular_matrix(main_matrix):
    del main_matrix[0]
    del main_matrix[-1]
    for row_index, row in enumerate(main_matrix):
        for col_index, col_val in enumerate(row):
            if col_index == 0 or col_index == (len(main_matrix[row_index]) - 1):
                del row[col_index]
    return main_matrix

def assign_tiles(matrix):
    indexing1 = (-1,0,1)
    for index_row, row_val in enumerate(matrix):
        if index_row == 0 or index_row == (len(matrix) - 1): # This omits the 0's we added to facilitate the process of counting the surrounding tiles
            continue
        for index_col, col_val in enumerate(row_val):
            if index_col == 0 or index_col == (len(row_val)-1): # ^^^
                continue
            elif col_val == 'X':
                continue
            else:
                for index1 in indexing1:
                    for index2 in indexing1: 
                        if matrix[index_row + index1][index_col + index2] == 'X':
                            row_val[index_col] += 1
                        else:
                            pass
    return matrix     

# Create a dictionary with all the coordinates and their respecting values
def coordinate_dictionary_with_keys(main_matrix):
    dict1 = {}
    dict2 = {}
    list1 = []
    for row_index, row_val in enumerate(main_matrix):
        val1 = int(list_of_Prime_numbers[row_index])
        list1.append([])
        for col_index, col_val in enumerate(row_val):
            val2 = int(list_of_Prime_numbers[(len(main_matrix)) + col_index])
            dict1[str(val1*val2)] = (row_index,col_index+1)
            dict2[f'{val1} x {val2}'] = (row_index,col_index+1)
            list1[row_index].append((row_index,col_index+1))
    return dict1,dict2,list1

def check_ceroes(start_index,main_matrix,player_matrix):
    indexing1 = (-1,0,1)
    ceroes_queue,ceroes_checked = [start_index], []
    for indece_value in ceroes_queue:
        if indece_value in ceroes_checked:
            continue
        for index1 in indexing1:
            for index2 in indexing1:
                row_index = indece_value[0]+index1
                col_index = indece_value[1] + index2
                reveal_val = main_matrix[row_index][col_index]
                if reveal_val != 'X':
                    player_matrix[row_index][col_index] = reveal_val
                if reveal_val == 0 and tuple((row_index,col_index)) not in ceroes_checked:
                    ceroes_queue.append((row_index,col_index))             
        ceroes_checked.append(indece_value)
    return regular_matrix(main_matrix), regular_matrix(player_matrix)
