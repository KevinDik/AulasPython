cond = int(input('Digite o número final '))
#Programa principal
for numero in range(cond, 0, -1):
    if numero % 3 == 1:
        print(numero)
