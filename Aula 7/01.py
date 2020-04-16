from time import sleep
vetores = list()
for valor in range(1, 7):
    itens = int(input('Digite um número: '))
    vetores.append(itens)
    print('Valor adicionado com sucesso')
    sleep(0.3)
print(f'Valores inseridos: {vetores}')
soma = vetores[0] + vetores[1] + vetores[5]
print(f'A soma dos valores dos itens 0, 1, 5 é de: {soma}')
vetores[4] = 100
for valor in vetores:
    print(f'Valores: {valor}')
