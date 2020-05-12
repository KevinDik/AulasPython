from random import randint

vetor = []
for c in range(1, 11):
    vetor.append(randint(1, 30))
print(f'Vetor soteado: {vetor}')
vetor.sort()
print(f'Vetor ordenado: {vetor}')