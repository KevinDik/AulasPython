from random import randint
vetor = [randint(1, 20) for valor in range(11)]
print(vetor)
for pos, valor in enumerate(vetor):
    if valor % 2 != 0 or valor == 2:
        print(f'Valor primo {valor} na posição {pos}')