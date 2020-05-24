def simplificador(numerador, denominador):
    """
    Função que calcula o maximo divisor comun dos numeros digitados e simplifica a fração
    :param numerador: numerador da fração
    :param denominador: denominador da fração
    :return: retorna um print explicando o resultado obitido
    """
    numero1 = set()
    numero2 = set()
    total = 0
    for c in range(1, numerador+1):
        numero1.add(c)
    for c in range(1, denominador+1):
        numero2.add(c)
    intersecao = numero1.intersection(numero2)
    for numero in intersecao:
        if numerador % numero == 0:
            if denominador % numero == 0:
                total = numero
    return print(f'Simplificando a fração digitada {numerador}/{denominador} pelo máximo divisor comun {total},'
                 f' será de {numerador/total:.0f}/{denominador/total:.0f}')


# Programa Principal
numerador = int(input('Digite o númerador: '))
denominador = int(input('Digite o denominador: '))
simplificador(numerador, denominador)