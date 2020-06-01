vetor = [int(input('Digite um número: ')) for valor in range(1, 11)]
print('Valores adicionados', vetor)
print('Lista de valores pares: ')
[print(valor, end=' ') for valor in vetor if not valor % 2]
