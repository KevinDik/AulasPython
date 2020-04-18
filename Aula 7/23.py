from random import randint
x = []
y = []
for c in range(1, 6):
    x.append(randint(1, 10))
    y.append(randint(1, 10))
print('Valor do conjunto X: ', x)
print('Valor do conjunto Y', y)
controle = 0
local = 0
while controle != 5:
    local += x[controle] * y[controle]
    controle += 1
print('Produto escalar resultante dos valores é de: ', local)
