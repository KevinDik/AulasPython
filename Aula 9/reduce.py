from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

mult = lambda x, y: x * y

res = reduce(mult, dados)
print(f' {res} ')

print('---')

res = 1
for n in dados:
    res = res * n
print(res)