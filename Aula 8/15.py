def triangulo(a, b, c):
    """
    função que indentifica se é triangulo e qual será seu tipo
    :param a: primeiro vertice
    :param b: segundo vertice
    :param c: terceiro vertice
    :return: retorna qual triangulo foi formado
    """
    if a < b + c and b < a + c and c < a + b:
        print('Formação de triangulo correta.')
    if a == b == c:
        return print('Triângulo equilátero')
    elif a == b or a == c  or c == b:
        return print('Triângulo isóceles')
    elif a != b and a != c and c != b:
        return print('Triângulo escaleno')


#Programa principal
while True:
    a = int(input('Primeiro lado: '))
    if a < 0:
        print('Número inválido')
    else:
        b = int(input('Segundo lado: '))
        if b < 0:
            print('Número inválido')
        else:
            c = int(input('Terceiro lado: '))
            if c < 0:
                print('Número inválido')
            triangulo(a, b, c)
            break
