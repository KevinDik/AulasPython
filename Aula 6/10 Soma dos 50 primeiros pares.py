numero = soma = 1
lista = []
while True:
    if numero % 2 == 0:
        lista.append(numero)
    numero += 1
    if numero == 51:
        break
print(sum(lista))
