# -*- coding: utf-8 -*-
"""
Tarea 4: Programas que usan repeticiones for

by Gabriel M - A01638293
"""

import random

Correct_num = random.randrange(0,101)
# print(Correct_num)

print('I have a number chosen between 1 and 100.')

guess = int(input('Please guess a number between 1 and 100: '))
attemps = 0

while guess != Correct_num:
    if guess < Correct_num:
        guess = int(input(f'I’m sorry but {guess} is too low, try again: '))
        
    else:
        guess = int(input(f'I’m sorry but is {guess} too high, try again: '))
        
    attemps += 1
    
print('You got it! The right answer is indeed', Correct_num,'.\nYou made',attemps,'guesses to get the right number.')
