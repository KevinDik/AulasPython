def volumeesfera(raio):
    """
    calcula o volume da esfera
    :param raio: raio a ser inserido
    :return: retorna um print com o volume informado de acordo com o raio
    """
    volume = 4/3 * 3.14 * (raio ** 3)
    return print(f'O volume da esfera é de {volume:.2f}')


volumeesfera(float(input('Digite o raio da esfera para saber seu volume: ')))