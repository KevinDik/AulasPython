valores = []
controle = 0
while controle != 6:
    num = int(input('Digite um valor PAR: '))
    if num % 2 == 0:
        valores.append(num)
        print('Valor adicionado')
        controle += 1
    else:
        print('Valor não adicionado')
print(f'Valores adicionados: {valores}')
valores.reverse()
print('Valores em orgem reversa', valores)