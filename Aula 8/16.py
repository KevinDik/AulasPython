def desenhar_linha(simbolo, quantidade=0):
    """
    Função que desenha uma linha de acordo com o informado
    :param simbolo: simbolo a ser desenhado
    :param quantidade: quantas repetições
    :return: retorna a linha conforme parametrizada
    """
    return print(f'{simbolo}' * quantidade)


# Programa principal
desenhar_linha('*', 50)
