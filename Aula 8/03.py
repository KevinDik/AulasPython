def vernum(valor):
    """
    Função que retorna 0 para numeros negativos e 1 para poistivos
    :param valor: numero a ser analisado
    :return: retorna 0 ou 1 conforme prescrito
    """
    if valor < 0:
        return 0
    else:
        return 1


num = vernum(int(input('Digite um número: ')))
if num == 0:
    print('Número negativo digitado')
else:
    print('Número positivo digitado')
