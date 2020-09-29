'''
iterators and iterables

iterator: objeto que pode ser iterado
          objeto que retorna um dado sendo um elemento por vez quando uma funcao next é chamada

iterable: objeto que retorna um iterator quando a funcao iter() for chamada

nome = 'geek' # um iterable mas nao é um iterator
numeros = [1, 2, 3, 4, 5, 6] # um iterable mas nao é um iterator

print(nome)
print(numeros)

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1)) # G
print(next(it1)) # E
print(next(it1)) # E
print(next(it1)) # K

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
'''

nome = 'geek' # um iterable mas nao é um iterator
for letra in nome:
    print(letra)
