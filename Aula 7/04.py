vetor = []
for item in range(1, 9):
    num = int(input('Digite um número para adicionar ao vetor: '))
    vetor.append(num)
print(f'Lista de valores adicionados na lista: {vetor}')
x = int(input('Digite a primeira posição: '))
y = int(input('Digite a segunda posição: '))
soma = vetor[x] + vetor[y]
print(f'A soma dos valores nas posições {x} e {y} é de {soma}')