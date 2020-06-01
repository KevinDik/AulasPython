lista = list(int(input('Digite um valor: ')) for valor in range(1, 7))
print(f'Os valores digitados foram: ')
[print(valor, end=' ') for valor in lista]
