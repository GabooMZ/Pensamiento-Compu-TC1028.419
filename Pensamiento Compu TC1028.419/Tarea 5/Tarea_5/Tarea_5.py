'''
Tarea 5: Programas que utilizan listas

Create a program that asks the user for 10 numbers  (floating point). 
Store those numbers in a list. Show to the user the total, average and standard deviation of those numbers.

Gabriel Melendez - A01638293
'''

l = [] #main list/dataset
total = 0
stdev = 0 
avg = 0

for x in range(1,11):
     num = float(input(f'{x}. Give me a number: '))
     total += num
     l.append(num)

avg = total/len(l)
sum_of_sqrs = 0
l2 = [] # this list is for the deviation of each number


for num in l:
    Xi = num - avg #Deviation from the mean
    Xi = Xi**2 # Squared deviation from the mean
    sum_of_sqrs += Xi

stdev = sum_of_sqrs/len(l)

print(f'The total is: {total}\nThe average is: {avg}\nThe Standard Deviation is: {stdev}')


    




