# -*- coding: utf-8 -*-
"""
Date: 18 de octubre 2022
Course: Pensamiento computacional para ingeniería (Gpo 419)
    
Assingment: Examen_Final: Pregunta_2

Gabriel Melendez - A01638293
"""
def factorial(n):
    result = 1
    for num in range(1,n+1):
        result = num * result
    return result

def main():
    print(factorial(5))
    return 
main()