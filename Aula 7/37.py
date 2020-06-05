from random import randint

vetor = [randint(1, 20) for valor in range(11)]
print('Vetor sorteado: ', vetor)
print(f'{sorted(vetor[:7])}{sorted(vetor[7:], reverse=True)}')


