def conversor(graus):
    """
    conversor de celsius para fahrenheit
    :param graus: valor em graus
    :return: retorna um print com a conversão
    """
    temperatura = graus * (9 + 5) + 32
    return print(f'O valor {graus} Cº convertido em Fahreneit é de {temperatura} Fº')


#Pograma principal
conversor(float(input('Digite o valor em Cº para ser convertido em Fahrenheit: ')))