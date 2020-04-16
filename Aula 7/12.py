from random import randint
valores = []
for item in range(1, 6):
    valores.append(randint(-100, 100))
print('Valores escolhidos', valores)
print('Maior valor: ', max(valores))
print('Menor valor', min(valores))
print('Media de valores escolhidos', sum(valores) / len(valores))