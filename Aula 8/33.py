def somaAl(valor):
    from math import factorial
    numero = factorial(valor)
    soma = 0
    print('Valor do fatorial: ', numero)
    print('Soma dos algarismos é de: ', end='')
    for num in range(len(str(numero))):
        unidade = numero % 10
        numero = (numero - unidade) / 10
        soma += unidade
    print(f'{soma:.0f}', end='')





# Programa principal
somaAl(int(input('Digite um número para ver sua soma fatorial: ')))