from math import pow
reais = list()
quadrado = list()
for valor in range(1, 11):
    numero = int(input('Digite um valor: '))
    reais.append(numero)
for item in reais:
    n = pow(4, item)
    quadrado.append(n)
print(f'Os valores digitados foram: {reais}')
print(f'Os quadrados são: {quadrado}')
