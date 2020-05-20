def fatorial(valor):
    from math import factorial
    return print(f'O fatorial do número {valor} é de {factorial(valor)}')


#Programa principal
valor = int(input('Digite um numero para saber seu fatorial: '))
fatorial(valor)
