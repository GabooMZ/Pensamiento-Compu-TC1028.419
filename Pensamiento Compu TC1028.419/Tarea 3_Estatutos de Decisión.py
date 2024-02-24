# -*- coding: utf-8 -*-
"""
Tarea 2:
    
Estatutos de Decisión

by Gabriel M - A01638293
"""

def ºF_to_ºC():
    F = int(input('Please enter the temperature in Fahrenheit: '))
    C = (F - 32) * 5/9
    if C >= 100:
        water = 'Water does boil at this temperature'
    else:
        water = 'Water does not boil at this temperature'
    # State = 'Solid' if C <= 0 else State = 'Liquid'

    if C < 0:
        state = 'The state of Water at '+ str(C) +' is Solid'
    elif C >= 0 and C < 100:
        state = 'The state of Water at '+ str(C) +' is liquid'
    else:
        state = 'The state of Water at '+ str(C) +' is Gas'
    
    return '\nThe temperature in Celsius is '+str(C)+ '\n'+water +'\n'+state

def ºC_to_ºF():
    C = int(input('Please enter the temperature in Celsius: '))
    F = (C * 9/5) + 32
    if C >= 100:
        water = 'Water does boil at this temperature'
    else:
        water = 'Water does not boil at this temperature'
        
    if C < 0:
        state = 'The state of Water at '+ str(C) +' is Solid'
    elif C >= 0 and C < 100:
        state = 'The state of Water at '+ str(C) +' is liquid'
    else:
        state = 'The state of Water at '+ str(C) +' is Gas'
        
    
    
    return '\nThe temperature in Fahrenheit is '+str(F)+'\n'+water +'\n'+state

choice = input('Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\nYour choice: ')

x = 'Not a valid input'

if choice == 'C' or choice == 'c':
    x = ºF_to_ºC()
elif choice == 'F' or choice == 'f':
    x = ºC_to_ºF()
print(x)
   