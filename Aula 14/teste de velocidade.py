'''
teste de velocidade com expressoes geradoras
# generators
def nums():
    for num in range(1, 10):
        yield num


g1 = nums()
print(g1)

print(next(g1))
print(next(g1))
print(next(g1))

#generator expression
g2 = (num for num in range(1, 10))
print(next(g2))
print(g2)
print(next(g2))
print(next(g2))

print(sum(num for num in range(1, 10)))

'''

import time

#generator expression
gen_inicio = time.time()
print(sum(num for num in range(100000000))) # 100 milhoes
gen_tempo = time.time() - gen_inicio

#list comprention
list_inicio = time.time()
print(sum(num for num in range(100000000))) # 100 milhoes
list_tempo = time.time() - list_inicio

print('generator expression', gen_tempo)
print('list compreention', list_tempo)
