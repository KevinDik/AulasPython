from random import randint
valores = [randint(-100, 100) for valor in range(1, 6)]
print('Valores digitados', valores)
print(f'Maior valor randomizado {max(valores)}, na posição: {valores.index(max(valores))}')
print(f'Menor valor randomizado {min(valores)}, na posição: {valores.index(min(valores))}')