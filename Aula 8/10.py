def saber_maior(valor1, valor2):
    """
    informa quem é o maior de acordo com os parametros
    :param valor1: numero um
    :param valor2: segundo numero
    :return: retorna o maior escrito e formatado
    """
    if valor1 > valor2:
        return print(f'O {valor1} é maior que o {valor2}')
    elif valor1 < valor2:
        return print(f'O {valor2} é maior que o {valor1}')


#Programa principal
print('-'*40)
print('Saber qual é o maior'. center(40))
print('-'*40)
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
saber_maior(a, b)