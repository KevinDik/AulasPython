from random import randint

vetor1 = set(randint(1, 50) for valor in range(11))
vetor2 = set(randint(1, 50) for vet in range(11))

print('Primeiro vetor sorteado: ', vetor1)
print('Segundo vetor sorteado: ', vetor2)

vetor3 = vetor1.union(vetor2)
print('Vetor de união: ', vetor3)