def formar_linhas(valor):
    controle = 1
    for c in range(0, valor):
        print('!' * controle)
        controle += 1


# Programa Principal
valor = int(input('Digite um parametro: '))
formar_linhas(valor)
