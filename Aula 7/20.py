par = []
impar = []
vetor = []
for c in range(1, 51):
    vetor.append(c)
    if c % 2 == 0:
        par.append(c)
    elif c % 2 == 1:
        impar.append(c)
print(f'Vetor completo: {vetor}')
print(f'Vetor par {par}')
print(f'Vetor impar {impar}')