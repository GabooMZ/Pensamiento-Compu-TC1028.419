# -*- coding: utf-8 -*-
"""
Master Quiz pt 2

Gabriel Melendez
"""

alumnos = {}
sum_of_val = 0

for num in range(1,4):
    name = input(f'Cual es el nombre del alumno {num}: ')
    calificacion = int(input(f'Cual es la calificacion de {name}: '))
    alumnos[name] = calificacion

for key, value in alumnos.items():
    print(key, '\n', value)
    sum_of_val += float(value) 

prom = sum_of_val/3
print('Promedio\n', prom)