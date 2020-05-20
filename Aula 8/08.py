def hipotenusa(a, b):
    """
    função que retorna a hipotenusa dados dois valores
    :param a: um dos catetos
    :param b: um dos catetos
    :return: retorna um print informando sua hipotenusa
    """
    from math import hypot
    from time import sleep
    print('Calculando a hipotenusa', end='')
    for c in range(1, 4):
        print('.', end='')
        sleep(1)
    print()
    return print(f'Dados os valores do triangulo {a} e {b}, sua hipotenusa é de {hypot(a, b):.2f}')


#Programa Principal
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
hipotenusa(a, b)