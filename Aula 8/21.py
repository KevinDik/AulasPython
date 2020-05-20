def quant_primos(n):
    primo = []
    for c in range(1, n+1):
        if c % 2 != 0:
            primo.append(c)
    print(f'Números primos abaixo de {n}')
    for c in primo:
        print(c, end=' ')


# Programa principal
valor = int(input('Digite um número: '))
quant_primos(valor)
