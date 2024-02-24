# -*- coding: utf-8 -*-
"""
Date:
Course: Pensamiento computacional
    
Assingment: Proyecto Integrador

Gabriel Melendez - A01638293
Guillermo Villegas - A01637179
Cesar Adrian - A01643011
"""
# Hard 24x20 - 99 mines
# Medium 18x15 - 40 mines
# Easy 10x8 - 10 mines

from random import randint
# from time import sleep

 #                    ___           ___           ___           ___     
 #     _____         /__/\         /  /\         /  /\         /  /\    
 #    /  /::\        \  \:\       /  /:/_       /  /:/        /  /::\   
 #   /  /:/\:\        \  \:\     /  /:/ /\     /  /:/        /  /:/\:\  
 #  /  /:/~/::\   ___  \  \:\   /  /:/ /::\   /  /:/  ___   /  /:/~/::\ 
 # /__/:/ /:/\:| /__/\  \__\:\ /__/:/ /:/\:\ /__/:/  /  /\ /__/:/ /:/\:\
 # \  \:\/:/~/:/ \  \:\ /  /:/ \  \:\/:/~/:/ \  \:\ /  /:/ \  \:\/:/__\/
 #  \  \::/ /:/   \  \:\  /:/   \  \::/ /:/   \  \:\  /:/   \  \::/     
 #   \  \:\/:/     \  \:\/:/     \__\/ /:/     \  \:\/:/     \  \:\     
 #    \  \::/       \  \::/        /__/:/       \  \::/       \  \:\    
 #     \__\/         \__\/         \__\/         \__\/         \__\/       
# ==========================================================================================
# ----------------------------------------TO DO LIST----------------------------------------
# ==========================================================================================
# 1. STARTER TILE *CANNOT* BE A MINE (CURRENTLY YOU CAN HIT A MINE FROM THE START) (*QOL*)
# 2. INTRO LOGO; LOGOS FOR DESIGN PURPOSES (*QOL*)
# 5. A "You Win" or "You lose" accordingly
# 
# QOL = Quality of life
# ==========================================================================================
# --------------------------------FUNCTIONS FOR THE GAME------------------------------------
# ==========================================================================================
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
    
def print_board(size_Col, size_Row,main_matrix=None, ): #Prints the board in either difficulty it is given
    for i in range(size_Row ):
        print('\u001b[30;1m'+'̅ ̅ ̅ '+'\u001b[0m',end= '')
        for j in range(size_Col + 1):
            if j == size_Col:
                print('+',end='')
                continue
            print('+\u001b[30;1m---\u001b[0m', end='')
        print(f'\n{list_of_Prime_numbers[i]}', end = '')
        for row_index, element in enumerate(main_matrix):
            for col_index, value in enumerate(main_matrix[row_index]):  
                if i == (row_index): # This prints the values of the tiles with colors
                    if value == 'X':
                        print(f'| \u001b[30;1m{value}\u001b[0m ', end='') # This value show the mines
                    elif value == 'BR_X':
                        print('|\u001b[41;1m X \u001b[0m', end='')
                    elif value == 0:
                        print(f'| \u001b[0m{value}\u001b[0m ', end='')
                    elif value == 1:
                        print(f'| \u001b[34;1m{value}\u001b[0m ', end='')
                    elif value == 2:
                        print(f'| \u001b[32;1m{value}\u001b[0m ', end='')
                    elif value == 3:
                        print(f'| \u001b[31;1m{value}\u001b[0m ', end='')
                    elif value == 4:
                        print(f'| \u001b[35;1m{value}\u001b[0m ', end='')
                    elif value == 5:
                        print(f'| \u001b[33;1m{value}\u001b[0m ', end='')
                    elif value == 6:
                        print(f'| \u001b[36;1m{value}\u001b[0m ', end='')
                    elif value == 7:
                        print(f'| \u001b[30;1m{value}\u001b[0m ', end='')
                    elif value == 'F':
                        print(f'|\u001b[41;1m {value} \u001b[0m', end='')
                    else:
                        print('|   ', end='')
        print('|')
            

        #ESTA ES LA LIENA EN LA CUAL SE EDITARIA PARA PONER LA BANDERA O LA REVELACION
        # NADA MAS HAY Q AVERIGUAR EN Q COLUMNA Y FILA ES
    print('\u001b[30;1m'+'̅ ̅ ̅ '+'\u001b[0m', end= '')
    print('+\u001b[30;1m---\u001b[0m' * size_Col, end='+')
    print('\n   ',end='')
    
    list_of_Prime_numbers_2 = [int(k) for k in list_of_Prime_numbers]
    list_of_Prime_numbers_2 = [k for k in list_of_Prime_numbers_2 if k > list_of_Prime_numbers_2[i]]
     
    for counter, num in enumerate(list_of_Prime_numbers_2):
        if counter == size_Col:
            break
        elif num < 100:
            print(f'|{num} ',end= '')
        else:
            print(f'|{num}', end= '')
    print('|')
  
# This functions clears the Console
def clear():
    print("\033[H\033[2J", end="")
    return

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

# Returns the move of the player
def make_move(col, row, player_matrix): 
    print('\nType the product of the values you choose and add at the end an "f" or "r" each for Flag or Reveal\nEg:(121f)')
    while True:
        try:
            coordinate = input('What is the product of the values you choose: ')
            if 'f' in coordinate:
                new_str = coordinate.replace('f', '')
                new_str = int(new_str)
                decision = 'f'
            elif 'r' in coordinate:
                new_str = coordinate.replace('r', '')
                new_str = int(new_str)
                decision = 'r'
            elif coordinate == 'exit':
                return 'petatear'
            else:
                raise Exception('The value given can not be computed')
        except:
            clear()
            print_board(col, row, player_matrix)
            print(f'The value given CAN NOT be computed: {coordinate}')
            continue
        else:
            return str(new_str), decision

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
    for row_index, row_val in enumerate(main_matrix):
        val1 = int(list_of_Prime_numbers[row_index])
        for col_index, col_val in enumerate(row_val):
            val2 = int(list_of_Prime_numbers[(len(main_matrix)) + col_index])
            dict1[str(val1*val2)] = (row_index,col_index)
    return dict1

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
                player_matrix[row_index][col_index] = reveal_val
                if reveal_val == 0 and tuple((row_index,col_index)) not in ceroes_checked:
                    ceroes_queue.append((row_index,col_index))
             
        ceroes_checked.append(indece_value)
    return regular_matrix(main_matrix), regular_matrix(player_matrix)
# ==========================================================================================
# ------------------------MAIN FUNCTION FOR RUNNING THE GAME--------------------------------
# ==========================================================================================
def main():
    clear() 
    while True:
        try:
            mode = input('Hard(h)/Medium(m)/Easy(e)\nWhat difficulty do you want to play (Default - Easy): ')
            col, row, num_mines = gamemode(mode)
        except:
            print('Wrong input')
            continue
        else:
            clear()
            break
            
    main_matrix, player_matrix = assign_mines(listoflists_maker(col, row), num_mines), listoflists_maker(col, row, '')
    # print('main matrix')
    # [print(k) for k in main_matrix]
    # print('player matrix')
    # [print(k) for k in player_matrix]
    
    prep_matrix(main_matrix)
    assign_tiles(main_matrix)
    regular_matrix(main_matrix)
    main_dict = coordinate_dictionary_with_keys(main_matrix)
    # print('main matrix')
    # [print(k) for k in main_matrix]
    # print('main dict')
    # print(main_dict)
    
    while True:
        print(player_matrix)
        print_board(col, row, player_matrix)
        try:
            coordinate, decision = make_move(col, row, player_matrix)
        except:
            # clear()
            print_board(col, row, player_matrix)
            print('Game Exited')
            break
        if coordinate not in main_dict: # if the number given does not match a coordinate reiterate
            # clear()
            continue
        else:
            indeces = main_dict[coordinate]
            print(indeces)
            if main_matrix[indeces[0]][indeces[1]] != 'X' and decision == 'r': # MAIN - Reveal tile
                if main_matrix[indeces[0]][indeces[1]] == 0: # If you hit a 0 reveal surrounding tiles
                    main_matrix = prep_matrix(main_matrix)
                    player_matrix = prep_matrix(player_matrix)
                    sample_indeces = [k+1 for k in indeces]
                    main_matrix,player_matrix = check_ceroes(sample_indeces, main_matrix, player_matrix)
                else: # Reveal the tile you choose if not 0
                    player_matrix[indeces[0]][indeces[1]] = main_matrix[indeces[0]][indeces[1]]
                
            elif decision == 'f' and player_matrix[indeces[0]][indeces[1]] != 'F': # Flag Tile
                player_matrix[indeces[0]][indeces[1]] = 'F'
                
            elif decision == 'f' and player_matrix[indeces[0]][indeces[1]] == 'F': # Unflag tile
                player_matrix[indeces[0]][indeces[1]] = ''
                
            else: # This ends the game by showing the mines and ending the loop
                for values in main_dict.values():
                    if main_matrix[values[0]][values[1]] != 'X':
                        continue
                    else:
                        if values[0] == indeces[0] and values[1] ==indeces[1]:
                            player_matrix[values[0]][values[1]] = 'BR_X'
                        else:
                            player_matrix[values[0]][values[1]] = main_matrix[values[0]][values[1]]
                # clear()
                print_board(col, row, player_matrix)
                print('\nYOU LOSEEEEE') # ************Smt funny here to say they lost*******
                break
            # clear()
    return
main()