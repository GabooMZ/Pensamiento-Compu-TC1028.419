# -*- coding: utf-8 -*-
"""
Date: 18 de octubre 2022
Course: Pensamiento computacional para ingeniería (Gpo 419)
    
Assingment: Examen_Final: Pregunta_1

Gabriel Melendez - A01638293
"""
# =============================================================================
# Pregunta 1
# =============================================================================
def solo_primero(name_list):
    new_list = []
    for name in name_list:
        if name in new_list:
            continue
        new_list.append(name)
    return new_list

def main():
    print(solo_primero(['diego','diego','azael','karla','diego','azael']))
    return 

main()