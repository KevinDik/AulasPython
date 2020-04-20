from random import randint
vetor = []

for c in range(1, 11):
    vetor.append(randint(1, 30))
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