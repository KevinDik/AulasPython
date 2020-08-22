lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(res)
print(type(res))

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

for letra in reversed('Geek university'):
    print(letra, end='')
print()
letra = 'geek university'
[print(letra, end='') for letra in letra]
print()
print(''.join(list(reversed('Geek university'))))

print('geek university'[::-1])

for n in reversed(range(0, 10)):
    print(n, end='')
for n in range(9, -1, -1):
    print(n, end='')