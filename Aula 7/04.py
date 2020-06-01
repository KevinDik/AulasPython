vetor = [int(input('Digite um número para adicionar ao vetor: ')) for valor in range(1, 9)]
print(f'Lista de valores adicionados na lista: {vetor}')
x = int(input('Digite a primeira posição: '))
y = int(input('Digite a segunda posição: '))
soma = vetor[x] + vetor[y]
print(f'A soma dos valores nas posições:\nValor: {vetor[x]} posição {x} e valor{vetor[y]} posição {y} é de {soma}')
