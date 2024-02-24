# -*- coding: utf-8 -*-
"""
Master Quiz pt 1

Gabriel Melendez - A01638293
"""

def cuadrado():
    l = int(input('Cual es el lado del Cuadrado: '))
    return 'El area del cuadrado es: ' + str(l**2)

def rectangulo():
    l = int(input('Cual es el lado del Rectangulo: '))
    h = int(input('Cual es la altura del Rectangulo: '))
    return 'El area del rectangulo es: ' + str(l*h)
def triangulo():
    l = int(input('Cual es el lado del triangulo: '))
    h = int(input('Cual es la altura del triangulo: '))
    return 'El area del Triangulo es: ' + str((l*h)/2)

 
figura = input('Cual de las siguientes figuras quiere calcular el área: Cuadrado, Rectangulo o Triangulo: ')
    
if figura == 'cuadrado' or figura == 'Cuadrado':
    print(cuadrado())
    
elif figura == 'Rectangulo' or figura == 'rectangulo':
    print(rectangulo())
    
elif figura == 'Triangulo' or figura == 'triangulo': 
    print(triangulo())
else: 
    print('Figura Invalida')

