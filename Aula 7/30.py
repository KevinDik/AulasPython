from random import randint

vetor1 = set()
vetor2 = set()

for item in range(1, 11):
    vetor1.add(randint(1, 50))
    vetor2.add(randint(1, 50))

print('Primeiro vetor sorteado: ', vetor1)
print('Segundo vetor sorteado: ', vetor2)

vetor3 = vetor1.intersection(vetor2)
print('Vetor de insetrseção: ', vetor3)