# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:17:53 2022

Quiz de Programación 3: Repeticiones while

Gabriel Melendez A01638293
"""

even_count = 0
while True:
    try:
        whole_num = int(input('Dame un numero entero: '))
        
        if whole_num%2 == 0:
            even_count += 1
            
        if whole_num < 0:
            print('Total de pares=', even_count)
            break
    except:
        continue
# =============================================================================
# %%
# =============================================================================
#sumatory = 0
#while true:
#    try:
#        whole_num = int(input('dame un numero para agregar a la suma: '))
        
#        if whole_num == -99:
#            print('la sumatoria es:', sumatory)
#            break
#        sumatory += whole_num
            
#    except:
#        continue