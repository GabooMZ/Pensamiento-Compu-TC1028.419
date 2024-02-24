import random
def lists_maker (col, row):

    main_list = []
    for i in range (row):
        main_list.append([])
        for n in range (col):
            
            main_list[i].append(0)

    return main_list

main = lists_maker(4,4)
for list in main:
    print(list)
print (len(main[0]))



def assign_mines(lists, num_mines):
#Esta función toma una lista de listas
#Ineserta n x´s en coordenadas aleatorias de la lista de listas
    counter = 0
    while counter != (num_mines): 
        row = random.randint(0,(len(lists)-1))
        col = random.randint(0,(len(lists[0])-1))
        if lists[row][col] != 'X':
           lists[row][col] = 'X'
        else:
           counter -= 1   
        counter += 1
    return (lists)

print(assign_mines(main, 3))

