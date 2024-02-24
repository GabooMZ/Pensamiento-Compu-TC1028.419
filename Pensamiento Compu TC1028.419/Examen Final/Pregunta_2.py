# -*- coding: utf-8 -*-
"""
Date: 18 de octubre 2022
Course: Pensamiento computacional para ingeniería (Gpo 419)
    
Assingment: Examen_Final: Pregunta_2

Gabriel Melendez - A01638293
"""
def cambiar_letras(phrase,fuente,destino):
    result = phrase.replace(fuente, destino)
    return result

def main():
    print(cambiar_letras('I really like my computer class', 'e', 'X'))
    return 
main()