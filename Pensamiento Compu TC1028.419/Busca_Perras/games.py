# -*- coding: utf-8 -*-
"""
Date:
Course:
    
Assingment:

Gabriel Melendez - A01638293
"""
import tkinter as tk
from only_functions import *
import tkinter.font as font

# ===========================================================================================
# GAME FUNCTIONS
# ===========================================================================================
def change_label(l):
    
    value = [i for i in label_dict if label_dict[i] == l]
    myFont = tk.font.Font(size=15,weight='bold')
    lbl_value["text"] = value[0]
    lbl_value['font'] = myFont

def reveal_tile(main_matrix, player_matrix,tile_matrix,mode):          
    pads = tile_dict[mode]
    coordinate_val = ent_coordinate.get()
    indeces = main_dict[coordinate_val]
    if coordinate_val in main_dict.keys():
        index = main_dict[coordinate_val]
        # print('INDEX',index)
        
        # [print(k) for k in main_matrix]
        # print('------------------------------')
        # [print(k) for k in player_matrix]
        # print(indeces)
        
        #If a 0 is revealed
        if player_matrix[indeces[0]][indeces[1]-1] == 'F':
            lbl_value["text"] = 'This tile is flagged, unflag it first to reveal'
            return
        if main_matrix[indeces[0]][indeces[1]-1] == 0:
            main_matrix = prep_matrix(main_matrix)
            player_matrix = prep_matrix(player_matrix)
            main_matrix, player_matrix = check_ceroes(indeces, main_matrix, player_matrix)
        
        else:
            reveal_val = main_matrix[index[0]][index[1]-1]
            player_matrix[index[0]][index[1]-1] = reveal_val
            # [print(k) for k in player_matrix]
            
        for main_index,(row_val,tile_index) in enumerate(zip(player_matrix,tile_matrix)):
            # print(main_index,row_val,tile_index)
            for second_index, main_val in enumerate(row_val):
                # print(main_val)
                if main_val != '':
                    frm_tile = tk.Frame(master=window,relief=tk.SUNKEN,padx=pads,pady=pads,borderwidth=2,bg='#e6e6e6')
                    
                    if main_val == 0:
                        lbl_tile = tk.Label(master=frm_tile,text='   ',bg='#e6e6e6')
                    elif main_val == 'F':
                        continue
                    else:
                        color = color_dict[main_val]
                        
                        lbl_tile = tk.Label(master=frm_tile,text=f' {main_val} ',fg=color,bg='#e6e6e6')
                        myFont = tk.font.Font(size=9,weight='bold')
                        lbl_tile['font'] = myFont
                        if main_val == 'X':
                            end_game(player_matrix,indeces,mode)
                            
                            return

                    for button in window.grid_slaves():
                        if int(button.grid_info()['row']) == tile_index[second_index][0] and int(button.grid_info()['column']) == tile_index[second_index][1]:
                            # print('FOUND BUTTON IN GRID: ',tile_index[second_index])
                            button.grid_forget()
                            frm_tile.grid(row=tile_index[second_index][0],column=tile_index[second_index][1])
                            lbl_tile.pack()
                            
                else:
                    continue
    
    ent_coordinate.delete(0,'end')
    
    win_check = 0
    win_val = {'easy': 10,'medium': 40, 'hard': 99}
    for row_index, row in enumerate(player_matrix):
        for col_index, col_val in enumerate(row):
            if win_check == win_val[mode]:
                win_screen() 
            elif (col_val == '' or player_matrix[row_index][col_index] == 'F') and main_matrix[row_index][col_index] == 'X':
                win_check += 1
            elif col_val == '' and main_matrix[row_index][col_index] != 'X':
                win_check -= 1
    # print('\n\n', win_check)
    # [print(k) for k in player_matrix]
    # [print(k) for k in main_matrix]
    return

def flag_tile(player_matrix,tile_matrix):
    
    coordinate_val = ent_coordinate.get()
    indeces = main_dict[coordinate_val]
    
    for row_val,tile_index in zip(player_matrix,tile_matrix):       
        for second_index, main_val in enumerate(row_val):
            if tile_index[second_index] == indeces:
                for button in window.grid_slaves():
                    if int(button.grid_info()['row']) == tile_index[second_index][0] and int(button.grid_info()['column']) == tile_index[second_index][1]:
                        text_val = button.cget('text')
                        if text_val == '   ':
                            myFont = tk.font.Font(size=9)
                            button['text'] = '🚩'
                            button['font'] = myFont
                            button['fg'] = 'red'
                            row_val[second_index] = 'F'
                        else:
                            button['text'] = '   '
                            row_val[second_index] = ''
            else:
                continue
    ent_coordinate.delete(0,'end')
    return

def window_reset():
    for button in window.grid_slaves():
        button.grid_forget()
    return


def end_game(player_matrix,indeces,mode):
    grid = {'easy':(9,0), 'medium':(16,0), 'hard':(21,0)}
    
    pads = tile_dict[mode]
    x_list = []
    for values in main_dict.values():
        if main_matrix[values[0]][values[1]-1] != 'X':
            continue
        else:
            for button in window.grid_slaves():
                frm_tile = tk.Frame(master=window,relief=tk.SUNKEN,padx=pads,pady=pads,borderwidth=4,bg='#e6e6e6')
                lbl_tile = tk.Label(master=frm_tile,text=' X ',fg='black',bg='#e6e6e6')
                if values not in x_list and int(button.grid_info()['row']) == values[0] and int(button.grid_info()['column']) == values[1]:
                    player_matrix[values[0]][values[1]-1] = main_matrix[values[0]][values[1]-1]
                    if int(button.grid_info()['row']) == indeces[0] and int(button.grid_info()['column']) == indeces[1] and indeces not in x_list:
                        player_matrix[values[0]][values[1]-1] = 'X'
                        frm_tile = tk.Frame(master=window,relief=tk.SUNKEN,padx=pads,pady=pads,borderwidth=4,bg='red')
                        lbl_tile = tk.Label(master=frm_tile,text=' X ',fg='black',bg='red')
                        myFont = tk.font.Font(size=9)
                        lbl_tile['font'] = myFont
                    
                    button.grid_forget()
                    frm_tile.grid(row=values[0],column=values[1])
                    lbl_tile.pack()
                    x_list.append(values)
                    break
    ent_coordinate.grid_remove()
    btn_flag.grid_remove()
    btn_reveal.grid_remove()
    lbl_value.grid_remove()
    btn_restart = tk.Button(master=window, text='BACK TO MENU',width=40,height=6, bg = 'blue', command = window_reset)
    btn_restart.grid(row=grid[mode][0],column=0, columnspan=20,sticky='w')
    
    return

def win_screen():
    return
# ============================================================================================
# # ===========================================================================================
# # MAIN GAME
# # ===========================================================================================
# ============================================================================================
list_of_Prime_numbers = ['02 ','03 ','05 ','07 ','11 ','13 ','17 ','19 ','23 ','29 ','31 ','37 ','41 ','43 ','47 ','53 ','59 ','61 ','67 ','71 ','73 ','79 ','83 ','89 ','97 ','101','103','107','109','113','127','131','137','139','149','151','157','163','167','173','179','181','191','193','197','199']
color_dict = {1:'blue',2:'green',3:'red',4:'purple',5:'yellow',6:'orange','X':'black'}
tile_dict = {'easy':22,'medium':6,'hard':0}
mode = 'easy'
col, row, num_mines = gamemode(mode)
main_matrix, player_matrix = assign_mines(listoflists_maker(col, row), num_mines), listoflists_maker(col, row, '')
prep_matrix(main_matrix)
assign_tiles(main_matrix)
regular_matrix(main_matrix)
main_dict, label_dict, tile_matrix = coordinate_dictionary_with_keys(main_matrix)
# print(main_dict)
# =============================================================================
# =============================================================================
if mode == 'easy':
    window = tk.Tk()

    lbl_value = tk.Label(master=window, text='¡PRESIONA UNA CASILLA!') #THIS LABEL FOR CHANGING THE PRODUCT WIDGET
    ent_coordinate = tk.Entry(master=window,width=40)
    btn_reveal = tk.Button(master=window, text='REVEAL',width=12,height=6,command= lambda x = main_matrix, y = player_matrix,z = tile_matrix, k= mode: reveal_tile(x,y,z,k))
    btn_flag = tk.Button(master=window, text='FLAG',width=12,height=6, command = lambda x = player_matrix, y = tile_matrix: flag_tile(x,y))

    lbl_value.grid(row=9,column=2, columnspan=4,sticky='S')
    ent_coordinate.grid(row=10,column=2, columnspan=4,sticky='NW')
    btn_reveal.grid(row=9,column=6,columnspan=2,rowspan=2)
    btn_flag.grid(row=9,column=8,columnspan=2,rowspan=2,sticky='W')

    for x in range(9):
        for y in range(11):
            if x == 8 and y== 0:
                continue
            if y == 0 and x != 8:
                coordinate_num = tk.Label(master=window,text=f'{list_of_Prime_numbers[x]}')
                coordinate_num.grid(row=x,column=y)
                continue
            if x == 8 and y != 0:
                coordinate_num = tk.Label(master=window,text=f'{list_of_Prime_numbers[y+7]}')
                coordinate_num.grid(row=x,column=y)
                continue
            
            blank_btn = tk.Button(master=window,text='   ',width=8,height=4, command=lambda l=(x,y): change_label(l))
            blank_btn.grid(row=x,column=y)
            
            
            # main_cell_location[****]
    window.mainloop()

if mode == 'medium':
    window = tk.Tk()
    
    lbl_value = tk.Label(master=window, text='¡PRESIONA UNA CASILLA!') #THIS LABEL FOR CHANGING THE PRODUCT WIDGET
    ent_coordinate = tk.Entry(master=window,width=40)
    btn_reveal = tk.Button(master=window, text='REVEAL',width=9,height=4,command= lambda x = main_matrix, y = player_matrix,z = tile_matrix,k= mode: reveal_tile(x,y,z,k))
    btn_flag = tk.Button(master=window, text='FLAG',width=9,height=4, command = lambda x = player_matrix, y = tile_matrix: flag_tile(x,y))

    lbl_value.grid(row=16,column=2, columnspan=7,sticky='S')
    ent_coordinate.grid(row=17,column=2, columnspan=7,sticky='NW')
    btn_reveal.grid(row=16,column=9,columnspan=2,rowspan=2)
    btn_flag.grid(row=16,column=11,columnspan=2,rowspan=2,sticky='W')
    
    for x in range(16):
        for y in range(19):
            frame = tk.Frame(master=window)
            if x == 15 and y== 0:
                continue
            if y == 0 and x != 15:
                frame = tk.Frame(master=window,borderwidth=1)
                coordinate_num = tk.Label(master=frame,text=f'{list_of_Prime_numbers[x]}')
                frame.grid(row=x,column=y)
                coordinate_num.pack()
                continue
            if x == 15 and y != 0:
                frame = tk.Frame(master=window,borderwidth=1)
                coordinate_num = tk.Label(master=frame,text=f'{list_of_Prime_numbers[y+14]}')
                frame.grid(row=x,column=y)
                coordinate_num.pack()
                continue
            blank_btn = tk.Button(master=window,text='   ',width=4,height=2, command=lambda l=(x,y): change_label(l))
            blank_btn.grid(row=x,column=y)
                       
    window.mainloop() 

if mode =='hard':
    window = tk.Tk()
    
    lbl_value = tk.Label(master=window, text='¡PRESIONA UNA CASILLA!') #THIS LABEL FOR CHANGING THE PRODUCT WIDGET
    ent_coordinate = tk.Entry(master=window,width=28)
    btn_reveal = tk.Button(master=window, text='REVEAL',width=8,height=4,command= lambda x = main_matrix, y = player_matrix,z = tile_matrix,k= mode: reveal_tile(x,y,z,k))
    btn_flag = tk.Button(master=window, text='FLAG',width=8,height=4, command = lambda x = player_matrix, y = tile_matrix: flag_tile(x,y))

    lbl_value.grid(row=21,column=2, columnspan=7,sticky='S')
    ent_coordinate.grid(row=22,column=2, columnspan=7,sticky='NW')
    btn_reveal.grid(row=21,column=10,columnspan=4,rowspan=2)
    btn_flag.grid(row=21,column=14,columnspan=4,rowspan=2,sticky='W')
    
    for x in range(21):
        for y in range(23):
            frame = tk.Frame(master=window)
            if x == 20 and y== 0:
                continue
            if y == 0 and x != 20:
                frame = tk.Frame(master=window,borderwidth=1)
                coordinate_num = tk.Label(master=frame,text=f'{list_of_Prime_numbers[x]}')
                frame.grid(row=x,column=y)
                coordinate_num.pack()
                continue
            if x == 20 and y != 0:
                frame = tk.Frame(master=window,borderwidth=1)
                coordinate_num = tk.Label(master=frame,text=f'{list_of_Prime_numbers[y+19]}')
                frame.grid(row=x,column=y)
                coordinate_num.pack()
                continue
            blank_btn = tk.Button(master=frame,relief=tk.RAISED,text='   ',
                                   width=2,height=1)
            
            blank_btn = tk.Button(master=window,text='   ',width=2,height=1, command=lambda l=(x,y): change_label(l))
            blank_btn.grid(row=x,column=y)
            
   
    window.mainloop()

