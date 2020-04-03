numero = int(input('Digite um número inteiro: '))
soma = 0
for c in range(1, numero):
    if numero % c == 0:
        soma += c
        print(f'{c}', end=' ')
print(f'A soma dos valores é de {soma}')
