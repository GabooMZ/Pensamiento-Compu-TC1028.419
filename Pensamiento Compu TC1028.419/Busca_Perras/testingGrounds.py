# -*- coding: utf-8 -*-
"""
Date:
Course:
    
Assingment:

Gabriel Melendez - A01638293
"""





# from os import system, name
# from time import sleep
# def clear():
#    # for windows
#    if name == 'nt':
#       _ = system('cls')

#    # for mac and linux
#    # else:
#        # _= system('clear')





# print('Hi Learner!!')
# sleep(2)
# clear()
# for x in range(10):
# #     print('+ - +\n|   |\n+ - +')\
# x = 5
# for i in range(x + 20):
#     print(i)





# for i in range(10):
#     list_of_Prime_numbers = [2,3,5,7,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]
# print(len(list_of_Prime_numbers))
# list_of_Prime_numbers_2 = [k for k in list_of_Prime_numbers if k > list_of_Prime_numbers[i]]
# print(list_of_Prime_numbers_2 )
# 
# import pandas as pd






# l = [2,5,'aldkfj',7,8,7,4,7,10]
# l2 = ['a','b','c','c','g','n','o','k']
l3 = [2,5,7]
print(len(l3))
tuple
# d = {'a': (1,2), 'b':2}
# a = 'a'
# if a in d:
    
#     g = d[a]
#     print('True', g[0])
# else:
#     print('false')

# for index, x in enumerate(l3):
#     print(type(index))
# print(len(l3))



# for x,y,z in zip(l,l2,l3):
#     print(x,y,z)




# for i, x in enumerate(l):
#     Max = l.max()
#     if x is Max:
#         print(i,x)





# print('\u001b[31;1mHello World\u001b[0m')
# print('Hello World')




# import numpy as np

# print(l)




# def mine_counter(matrix):
#     for index, row_vals in enumerate(matrix):
#         matrix[index][:0] = ['0']
#         matrix[index].append('0')
#     matrix[:0] = [['0']*(len(row_vals))]
#     matrix.append((['0']*(len(row_vals))))
#     return matrix


# main_matrix = [['X','9','9'],['9','X','9'],['X','9','9']]
# for z in main_matrix:
#     print(z)
# main_matrix = mine_counter(main_matrix)
# for b in main_matrix:
#     print(b)

# for row_index, element in enumerate(main_matrix):
#     if row_index == 0 or row_index == (len(main_matrix) - 1):
#         continue
#     for col_index, value in enumerate(main_matrix[row_index]):  
#         if col_index == 0 or col_index == (len(main_matrix[row_index]) - 1):
#             continue
#         print(value)


# def prep_matrix(matrix): 
    
#     for index, row_vals in enumerate(matrix):
#         matrix[index][:0] = ['N']
#         matrix[index].append('N')
#     matrix[:0] = [['N']*(len(row_vals))]
#     matrix.append((['N']*(len(row_vals))))
#     return matrix

# # This function reverts what assign_tiles() does but keeps the values it modified
# def regular_matrix(main_matrix):
#     del main_matrix[0]
#     del main_matrix[-1]
#     for row_index, row in enumerate(main_matrix):
#         for col_index, col_val in enumerate(row):
#             if col_index == 0 or col_index == (len(main_matrix[row_index]) - 1):
#                 del row[col_index]
#     return main_matrix

# def listoflists_maker(col, row, val=0):
#     main_matrix = []
#     for i in range (row):
#         main_matrix.append([])
#         for n in range (col):
#             main_matrix[i].append(val)
#     return main_matrix

# l1 = listoflists_maker(3, 3)
# [print(k) for k in l1]
# prep_matrix(l1)
# [print(k) for k in l1]
# regular_matrix(l1)
# [print(k) for k in l1]