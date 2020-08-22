from random import randint

listas = [[randint(1, 10) for valor in range(3)] for numero in range(3)]
print(listas)

soma = lambda listas: