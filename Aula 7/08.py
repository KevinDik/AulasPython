from random import randint
valores = [randint(1, 100) for valor in range(1, 7)]
print(f'Número digitados foram: {valores}')
valores.reverse()
print(f'Sua ordem inversa é de {valores}')
