def desenhar_tri(valor):
    """
    desenha um triangulo em pe
    :param valor: tamanho do triangulo
    :return: desenha o triangulo com *
    """
    controle = 1
    espaco  = valor
    for c in range(1, valor):
        print(f'{" " * espaco}{"*" * controle}'.center(valor))
        controle += 2
        espaco -= 1


# Programa principal
desenhar_tri(int(input('Digite um valor: ')))
