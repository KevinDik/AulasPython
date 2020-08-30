'''import random
random.random() # gera num aleatorio entre 0 e 1
'''

from random import random; print(f'random {random()}')
from random import uniform; print(f'uniform {uniform(1, 7)}')
from random import randint; print(f'randint {randint(1, 10)}')
from random import choices; print(f'choices {choices(["pedra", "papel", "Tesoura"])}')
from random import shuffle;carta = ["8", "9", "5", "15"]; shuffle(carta); print(f'Shuffle {carta.pop()}')
