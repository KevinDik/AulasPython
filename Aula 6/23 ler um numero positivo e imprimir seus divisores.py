numero = int(input('Digite um número para saber seus divisores: '))
for c in range(1, numero+1):
    if numero % c == 0:
        print(c)
