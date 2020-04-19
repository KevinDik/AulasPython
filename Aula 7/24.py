from random import triangular
alunos = []
for pessoa in range(1, 11):
    alunos.append(triangular(1.5, 2.0))
print(alunos)
print(f'Maior aluno: {alunos.index(max(alunos))}, com o tamanho de {max(alunos):.2f}')
print(f'Menor aluno: {alunos.index(min(alunos))}, com o tamanho de {min(alunos):.2f}')
