# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# =============================================================================
import tkinter as tk
import random
    
window = tk.Tk()
# =============================================================================
# BORDER EFFECTS FOR TILE VISUALIZATION
# =============================================================================
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }
# 
# window = tk.Tk()
# 
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()
# =============================================================================

# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()

# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()

# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()

# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)

# # Bind keypress event to handle_keypress()
# # window.bind("<Key>", handle_keypress)

# def handle_click(event):
#     print("The button was clicked!")

# button = tk.Button(text="Click me!")
# button.pack()
# button.bind("<Button-1>", handle_click)

# def roll():
#     lbl_result["text"] = str(random.randint(1, 6))


# window.columnconfigure(0, minsize=150)
# window.rowconfigure([0, 1], minsize=50)

# btn_roll = tk.Button(text="Roll", command=roll)
# lbl_result = tk.Label()

# btn_roll.grid(row=0, column=0, sticky="nsew")
# lbl_result.grid(row=1, column=0)




# d1 = {'2 x 2': (1,1), '3 x 3': (2,2)}
# print(d1['2 x 2'])
color_dict = {1:'blue',2:'green',3:'red',4:'purple',5:'yellow',6:'orange'}
print(color_dict[1])


# window.mainloop()

