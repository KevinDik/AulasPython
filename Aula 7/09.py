valores = []
controle = 0
while controle != 6:
    numero = int(input('Digite um valor PAR: '))
    if valores[controle] % 2 == 0:
        print('Valor adicionado')
        controle += 1
        valores.append(numero)
    else:
        print('Valor não adicionado')
print(f'Valores adicionados: {valores}')
valores.reverse()
print('Valores em orgem reversa', valores)