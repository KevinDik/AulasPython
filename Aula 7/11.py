neg = soma = 0
vetor = [int(input('Digite um número real: ')) for valor in range(1, 11)]
[print(valor, end=' ') for valor in vetor]
for c in vetor:
    if c < 0:
        neg += 1
    if c > 0:
        soma += c
print('Valores negativos digitados ', neg)
print('Soma dos valores positivos ', soma)
