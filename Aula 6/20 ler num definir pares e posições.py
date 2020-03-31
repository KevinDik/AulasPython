lista = []
pares = []
while True:
    numero = int(input('Digite um número: [1000 para parar] '))
    if numero == 1000:
        break
    lista.append(numero)
for c in lista:
    if c % 2 == 0:
        pares.append(c)
print('-'*40)
print('Relatório de dados'.center(40))
print(f'Quantidade de valores digitados: {len(lista)}')
print(f'Valores digitados: {lista}')
print(f'Valores pares digitados: {pares}')
print('-'*40)
