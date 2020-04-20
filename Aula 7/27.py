from random import randint

vetor = []
for c in range(1, 11):
    vetor.append(randint(1, 20))
print(vetor)
for pos, valor in enumerate(vetor):
    if valor % 2 != 0:
        print(f'Valor primo {valor} na posição {pos}')