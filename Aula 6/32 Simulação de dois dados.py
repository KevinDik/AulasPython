from random import randint
from time import sleep
print('-' * 20)
print('Jogo dos dados'.center(20))
print('-' * 20)
sleep(1)
per = int(input('Quantas vezes os dados serão jogados: '))
for c in range(1, per+1):
    d1 = randint(1, 6)
    print(f'Jogando o primeiro dado', end='')
    for c in range(0, 3):
        print(f'.', end='')
        sleep(0.75)
    print(f' {d1}')
    d2 = randint(1, 6)
    print(f'Jogando o segundo dado', end='')
    for c in range(0, 3):
        print(f'.', end='')
        sleep(0.75)
    print(f' {d2}')
    print('-' * 20)
    print('RESULTADO'.center(20))
    print('-' * 20)
    if d1 > d2:
        print(f'O valor do {d1} do primeiro dado é MAIOR do que o {d2} valor do segundo dado')
    elif d1 == d2:
        print(f'Os valores do primeiro dado {d1} e segundo dado {d2} são iguais')
    else:
        print(f'O valor do {d1} do primeiro dado é MENOR do que o {d2} valor do segundo dado')
    print('-' * 20)