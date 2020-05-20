def exponencial(a, b):
    """
    Permite escolher a potencialização conforme os parametros
    :param a: numero base
    :param b: numero potencia
    :return: retorna o calculo conforme descrito em string
    """
    total = a ** b
    return print(f'Conforme digitado\n{a} com potência de {b} é igual à {total}')


# Programa principal
a = int(input('Digite a base da potencia: '))
b = int(input('Digite o expoente: '))
exponencial(a, b)
