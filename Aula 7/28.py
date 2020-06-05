from random import randint
vetor = [randint(1, 30) for valor in range(11)]
print('Vetor inicial', vetor)

vetorpar = vetor.copy()
vetorimpar = vetor.copy()

print('Vetor par:', end=' ')
for valor in vetorpar:
    if valor % 2 == 0:
        print(valor, end=' ')
print()
print('Vetor impar:', end=' ')
for valor in vetorimpar:
    if valor % 2 == 1:
        print(valor, end=' ')