def mat(valor1):
    from random import randint
    tabela = []
    for c in range(0, valor1):
        for q in range(0, valor1):
            tabela.append(randint(1, 20))
    for valor in tabela:
        print(f'  [ {valor} ]  ', end='')
    print()
    print('Valores maiores que 10: ')
    for valor in tabela:
        if valor > 10:
            print(valor, end=' ')


# Programa Principal
mat(int(input('Digite o tamanho da matriz: ')))
