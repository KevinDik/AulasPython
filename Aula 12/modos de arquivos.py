'''
r abre para leitura padrao
w abre para escrita sobrescreve caso ja exista
x abre para escrita somente se o arquivo nao existir
a abre para escrita adicionando o conteudo ao final do arquivo

'''

'''try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('teste de conteudo 2\n')
except FileExistsError:
    print('Arquivo ja criado')
'''
'''with open('fruta.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou SAIR: ')
        if fruta != 'SAIR':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
'''

with open('texto.txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('outro  dd novo topo \n')
    arquivo.write('outro dd  nova linha \n')
