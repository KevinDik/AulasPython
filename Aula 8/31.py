def neperiano(numero):
    """
    total = (1/numero!) = 1/0! + 1/1! + 1/2! ... 1/numero!
    :param numero: parametro n
    :return: retorna o calculo conforme visto acima
    """
    from math import factorial
    total = (1 / factorial(numero))
    for c in range(1, numero + 1):
        total += 1 / factorial(c)
    return print(f'De acordo com o número informado o total será de {total:2f}')


# Programa Principal
neperiano(int(input('Digite um número: ')))
