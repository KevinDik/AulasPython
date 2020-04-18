from random import triangular
alunos = []
cadastro = {}
for pessoa in range(1, 11):
    cadastro['Nº'] = pessoa
    cadastro['Altura'] = triangular(1.5, 2.0)
    alunos.append(cadastro.copy())
    cadastro.clear()
controle = 0
print(alunos)
for pessoa in alunos:
    if max(alunos[controle]["Altura"]):
        print(f'O maior aluno corresponde ao aluno nº {0} com a altura {alunos[controle]["Altura"]}')
    if min(alunos[controle]["Altura"]):
        print(f'O menor aluno corresponde ao aluno nº {0} com a altura {alunos[controle]["Altura"]}')
    controle += 1

