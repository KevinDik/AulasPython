from random import randint
x = [randint(1, 10) for valor in range(6)]
y = [randint(1, 10) for num in range(6)]
print('Valor do conjunto X: ', x)
print('Valor do conjunto Y', y)
controle = 0
local = 0
while controle != 5:
    local += x[controle] * y[controle]
    controle += 1
print('Produto escalar resultante dos valores é de: ', local)
