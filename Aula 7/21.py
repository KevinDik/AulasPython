from random import randint
a = [randint(1, 50) for valor in range(1, 11)]
b = [randint(1, 50) for numero in range(1, 11)]
c = []
controle = 0
while controle != 10:
    c.append(a[controle] - b[controle])
    controle += 1
print('Valor do vetor A:', a)
print('Valor do vetor B:', b)
print('Valor do vetor C:', c)
