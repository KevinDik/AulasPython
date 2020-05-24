def soma_algarismo(valor):
    controle = 1
    total = 1
    while controle < valor:
        total = controle * valor
        controle += 1
    print(total)



# Programa Principal
soma_algarismo(int(input('Digite um número para saber a soma fatorial de seus algarismos: ')))
