numeros = []
valor = int(input('Digite um número: '))
item = 1
while len(numeros) != 10:
    if item % valor == 0:
        numeros.append(item)
    item += 1
print(numeros)
