def cilindro(altura, raio):
    """
    Calcula o volume de acordo com os parametros
    :param altura: altura do circulo
    :param raio: raio do circulo
    :return: retorna um texto formatado com as especificações informadas
    """
    from time import sleep
    print('-'*40)
    print('Calculando', end='')
    for c in range(1, 4):
        print('.', end='')
        sleep(1)
    print()
    print('-' * 40)
    volume = 3.141592 * (raio ** 2) * altura
    return print(f'De acordo com os valores informados:\nAltura: {altura}\nRaio: {raio}\nO volume do circulo é de \033[31m{volume:.2f}\033[m')


#Programa principal
print('-'*40)
print('Calculador de volume para circulos'.center(40))
print('-'*40)
altura = float(input('Digite a altura: '))
raio = float(input('Digite o raio: '))
cilindro(altura, raio)