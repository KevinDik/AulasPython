vetor = []
neg = soma = 0
for c in range(1, 11):
    vetor.append(int(input('Digite um numero real: ')))
print(vetor)
for c in vetor:
    if c < 0:
        neg += 1
    if c > 0:
        soma += c
print('Valores negativos digitados ', neg)
print('Soma dos valores positivos ', soma)
