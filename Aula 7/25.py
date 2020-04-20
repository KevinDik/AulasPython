numeros = []
valor = 7
item = 1
while len(numeros) != 100:
    if item % valor == 0:
        numeros.append(item)
    item += 1
print(numeros)
