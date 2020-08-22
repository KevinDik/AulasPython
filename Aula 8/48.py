from random import randint
#matriz = [[], [], [], [], [], [], [], [], []]

matriz = [[randint(1, 20) for valor in range(3)]for num in range(3)]
for pos, valor in matriz:
    for item in valor:
        print(item, end=' ')
        if pos == 2 or 5 or 8:
            print()



