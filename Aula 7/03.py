reais = list(int(input('Digite um valor: ')) for valor in range(1, 11))
quadrado = [valor ** 4 for valor in reais]
print(f'Os valores digitados foram: {reais}')
print(f'Os quadrados são: {quadrado}')
