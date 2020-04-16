vetor = []
for c in range(1, 11):
    vetor.append(int(input('Digite um número: ')))
print('Valores adicionados', vetor)
print('Lista de valores pares: ')
for c in vetor:
    if c % 2 == 0:
        print(c, end=' ')