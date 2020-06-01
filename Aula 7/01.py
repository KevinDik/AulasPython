from time import sleep
vetores = []
while not vetores:
    try:
        vetores = list(int(input('Digite um número: ')) for numero in range(1, 7))
        sleep(0.3)
    except ValueError:
        print('Erro! Valor inserido é inválido')
        continue
print(f'Valores inseridos: {vetores}')
soma = vetores[0] + vetores[1] + vetores[5]
print(f'A soma dos valores dos itens 0, 1, 5 é de: {soma}')
vetores[4] = 100
[print(valor) for valor in vetores]
