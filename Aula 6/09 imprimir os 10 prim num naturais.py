nat = int(input('Informe um valor: '))
par = []
impar = []
for c in range(1, nat):
    if c % 3 == 0:
        impar.append(c)
    if c % 2 == 0:
        par.append(c)

print(f'Os números impares naturais são: {impar}')
print(f'Os números pares naturais são: {par}')
