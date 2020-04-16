from collections import Counter
from random import randint

lista = list()
for c in range(1, 11):
    lista.append(randint(1, 5))
print('Valores sorteados', lista)
for c in Counter(lista):
    print(f'O valor {c} repetiu {lista.count(c)} vezes')
