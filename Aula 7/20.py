print('Vetor par: ', end='')
[print(valor, end=' ') for valor in range(1, 51) if valor % 2 == 0]
print('\nVetor impar: ', end='')
[print(valor, end=' ') for valor in range(1, 51) if valor % 2 == 1]
