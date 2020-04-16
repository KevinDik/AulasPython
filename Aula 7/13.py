from random import randint
valores = []
for c in range(1, 6):
    valores.append(randint(-100, 100))
print('Valores digitados', valores)
print(f'Maior valor randomizado {max(valores)}, na posição: {valores.index(max(valores))}')
print(f'Menor valor randomizado {min(valores)}, na posição: {valores.index(min(valores))}')