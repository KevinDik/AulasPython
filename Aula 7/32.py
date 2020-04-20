from random import randint

vetor1 = []
vetor2 = []

for c in range(1, 6):
    vetor1.append(randint(1, 20))
    vetor2.append(randint(1, 20))

print(f'Vetor um sorteado: {vetor1}')
print(f'Vetor dois sorteado: {vetor2}')

posicao = 0
soma = []
print('Soma dos valores informados em suas respectivas posições: ', end='')
while posicao != 5:
    soma = vetor1[posicao] + vetor2[posicao]
    posicao += 1
    print(soma, end=' ')
print()

posicao = 0
multiplicacao = []
print('Multiplicação dos valores informados em suas respectivas posições: ', end='')
while posicao != 5:
    multiplicacao = vetor1[posicao] * vetor2[posicao]
    posicao += 1
    print(multiplicacao, end=' ')
print()

posicao = 0
intersecao = []
print('Interseção dos valores informados em suas respectivas posições: ', end='')
while posicao != 5:
    intersecao = set(vetor1).intersection(vetor2)
    posicao += 1
print(intersecao, end=' ')
print()

posicao = 0
uniao = []
print('União dos valores informados em suas respectivas posições: ', end='')
while posicao != 5:
    uniao = set(vetor1).union(vetor2)
    posicao += 1
print(uniao, end=' ')
print()