from random import randint
vetor = [randint(1, 30) for valor in range(11)]
print(f'Vetor soteado: {vetor}')
vetor.sort()
print(f'Vetor ordenado: {vetor}')