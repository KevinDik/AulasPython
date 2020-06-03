from random import randint
valores = [randint(-100, 100) for valor in range(1, 6)]
print('Valores escolhidos', valores)
print('Maior valor: ', max(valores))
print('Menor valor', min(valores))
print('Media de valores escolhidos', sum(valores) / len(valores))