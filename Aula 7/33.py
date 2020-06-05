from random import randint
vetor = [randint(0, 10) for valor in range(16)]
print(f'Vetor principal: {vetor}')
for valor in vetor:
    if valor == 0:
        vetor.remove(valor)
print(f'Vetor comprimido: {vetor}')
