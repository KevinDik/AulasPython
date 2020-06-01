notas = []
while not notas:
    try:
        notas = [float(input(f'Digite a nota do {valor}# aluno: ')) for valor in range(1, 16)]
    except ValueError:
        print('Erro!, Valores invalidos inseridos')
        continue
print(f'Notas digitadas {notas}')
print(f'A média geral da sala é de {sum(notas)/len(notas):.2f}')
