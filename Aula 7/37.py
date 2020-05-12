from random import randint

vetor = []
for c in range(11):
    vetor.append(randint(1, 20))
print('Vetor sorteado: ', vetor)
print(f'{sorted(vetor[:7])}{sorted(vetor[7:], reverse=True)}')


