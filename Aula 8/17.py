def soma_entre(numero1, numero2):
    """
    Função que permite somar os numeros de acordo com os parametros de inicio e fim
    :param numero1: numero inicial
    :param numero2: numero final
    :return: retorna a soma em uma string formatada
    """
    total = 0
    for c in range(numero1, numero2+1):
        total += c
    return print(f'A soma dos valores entre {numero1} e {numero2} é de {total}')


# Programa principal
a = int(input('Digite o parametro inicial: '))
b = int(input('Digite o parametro final: '))
soma_entre(a, b)
