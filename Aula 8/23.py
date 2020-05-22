def tri_lateral(valor):
    """
    Desenha um triangulo lateral
    :param valor: tamanho do triangulo
    :return: triangulo desenhado em *
    """
    for c in range(1, valor+1):
        print('*' * c)
    for c in range(valor-1, 0, -1):
        print('*' * c)


# Programa Principal
tri_lateral(int(input('Digite um número: ')))
