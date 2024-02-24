# -*- coding: utf-8 -*-
"""
Date:
Course:
    
Assingment:

Gabriel Melendez - A01638293
"""
import tkinter as tk
import random
        
window = tk.Tk()
window.title('MineSweeper Menu')
window.resizable(width=False, height=False)
# window.rowconfigure(0, minsize=5000, weight=1) # For expanding the window
# window.columnconfigure(1, minsize=800, weight=1) # for expanding the window

frame = tk.Frame(master=window,relief=tk.RAISED,borderwidth=0)

title_lbl = tk.Label(master=frame,text='MINESWEEPER')
easy_btn = tk.Button(master=frame,text='EASY')
medium_btn = tk.Button(master=frame,text='MEDIUM')
hard_btn = tk.Button(master=frame,text='HARD')
how_to_play_btn = tk.Button(master=frame,text='HOW TO PLAY')
exit_btn = tk.Button(master=frame,text='EXIT')

menu_list = (title_lbl,easy_btn,medium_btn,hard_btn,how_to_play_btn,exit_btn)

for x in range(6):
    frame.grid(row=x,column=1)
    menu_list[x].pack(padx=5,pady=5,fill=tk.X)




window.mainloop()   
