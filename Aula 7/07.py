from random import randint
vetor = list(randint(1, 100) for valor in range(1, 11))
print('Valores digitados foram: ', vetor)
print(f'Maior valor digitado foi: {max(vetor)} na posição: {vetor.index(max(vetor))}')
