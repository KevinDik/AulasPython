print(all((0, 2)))
nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristiano']
print(all(nome[0] == 'C' for nome in nomes))

print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(all(num for num in [4, 2, 10, 6, 8] if num % 2 == 0))

print(any([0, False, 2, 3, 4]))
