def somatorio(n):
    """
    soma os numero de 1 ate n
    :param n: parametro de fim
    :return: retorna o somatorio conforme descrito
    """
    total = 0
    for c in range(1, n+1):
        total += c
    print(f'A soma dos numeros de {1} até {n} é de {total}')


# Programa principal
somatorio(int(input('Digite um número: ')))
