from random import randint
lista = [randint(1, 20) for c in range(20)]
print('Elementos sorteados: ', lista)
lista2 = set(lista)
print('Elementos sorteados sem repetições: ', lista2)
