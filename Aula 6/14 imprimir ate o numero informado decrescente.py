cond = int(input('Digite o número final '))

for numero in range(cond, 0, -1):
    if numero % 2 == 0:
        print(numero)
