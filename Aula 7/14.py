from collections import Counter
from random import randint
lista = list(randint(1, 5) for valor in range(1, 11))
print('Valores sorteados', lista)
[print(f'O valor {c} repetiu {lista.count(c)} vezes') for c in Counter(lista)]
