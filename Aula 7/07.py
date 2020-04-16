from random import randint
vetor = list()
for c in range(1, 11):
    vetor.append(randint(1, 100))
print('Valores digitados foram: ', vetor)
print(f'Maior valor digitado foi: {max(vetor)} na posição: {vetor.index(max(vetor))}')
