notas = []
for valor in range(1, 16):
    num = float(input(f'Digite a nota do {valor}# aluno: '))
    notas.append(num)
print(f'Notas digitadas {notas}')
print(f'A média geral da sala é de {sum(notas)/len(notas):.2f}')
