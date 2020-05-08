from random import randint
vetor = []
for c in range(1, 16):
    valor = (vetor.append(randint(0, 10)))
print(f'Vetor principal: {vetor}')
for valor in vetor:
    if valor == 0:
        vetor.remove(valor)
print(f'Vetor comprimido: {vetor}')
