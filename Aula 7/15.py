from random import randint
lista = []
for c in range(1, 21):
    lista.append(randint(1, 20))
print('Elementos sorteados: ', lista)
lista2 = set(lista)
print('Elementos sorteados sem repetições: ', lista2)
