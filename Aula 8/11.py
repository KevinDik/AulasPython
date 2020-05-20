def calcular_notas(nota1, nota2, nota3, letra):
    """
    calcula a media aritimetica ou a ponderada de acordo com os parametros
    :param nota1: primeira nota
    :param nota2: segunda nota
    :param nota3: terceira nota
    :param letra: letra para escolha da media
    :return: returna as notas e sua media de acordo com a escolha por meio de u print
    """
    if letra == 'a':
        media = (nota1 + nota2 + nota3) / 3
        return print(f'De acordo com as notas informadas\nnota 1: {nota1} | nota 2: {nota2} | nota 3: {nota3}'
                     f'\nSua média aritimetica é de {media:.2f}')
    elif letra == 'p':
        ponderada = ((nota1*1) + (nota2*2) + (nota3*3)) / 1 + 2 + 3
        return print(f'De acordo com as notas informadas\nnota 1: {nota1} | nota 2: {nota2} | nota 3: {nota3}'
                     f'\nSua média ponderada é de {ponderada:.2f}')


#Programa principal
print('*'*40)
print('NOTAS ALUNOS'.center(40))
print('*'*40)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
letra = str(input('Escolha um:\na - Média aritimiética\np - Média ponderada\n'))
calcular_notas(nota1, nota2, nota3, letra)
