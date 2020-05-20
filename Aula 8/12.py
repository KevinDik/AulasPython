def calculo(numero):
    """
    Programa que soma os algarismos digitados
    :param numero: numero que sera somado
    :return: retorna o valor somado de cada algarismo digitado
    """
    total = 0
    while numero > 0:
        resto = numero % 10
        numero = (numero - resto) / 10
        total += resto
    return print(f'A soma de seus valores é de {total}')


# Programa Principal
while True:
    try:
        numero = (int(input('Digite um número inteiro maior que zero: ')))
        if numero < 0:
            print('Erro! Digite um número válido')
        else:
            calculo(numero)
            break
    except ValueError:
        print('Não é possivel inserir letras ou caracteres especiais')
