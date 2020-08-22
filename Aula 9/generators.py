from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristiano', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(getsizeof(res))
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(getsizeof(res))

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gen = getsizeof(x * 10 for x in range(1000))

print(f'List {list_comp}')
print(f'SET {set_comp}')
print(f'Dict {dict_comp}')
print(f'Gen {gen}')

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)