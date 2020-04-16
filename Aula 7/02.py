lista = list()
for item in range(1, 7):
    num = int(input('Digite um valor: '))
    lista.append(num)
print(f'Os valores digitados foram: ')
for valor in lista:
    print(valor, end=' ')
