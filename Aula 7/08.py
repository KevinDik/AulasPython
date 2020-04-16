from random import randint
valores = []
for item in range(1, 7):
    num = randint(1, 100)
    valores.append(num)
print(f'Número digitados foram: {valores}')
valores.reverse()
print(f'Sua ordem inversa é de {valores}')