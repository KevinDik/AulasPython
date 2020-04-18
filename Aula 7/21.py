from random import randint
a = []
b = []
for c in range(1, 11):
    a.append(randint(1, 50))
    b.append(randint(1, 50))
c = []
controle = 0
while controle != 10:
    c.append(a[controle] - b[controle])
    controle += 1

print('Valor do vetor A:', a)
print('Valor do vetor B:', b)
print('Valor do vetor C:', c)
