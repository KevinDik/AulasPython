#arquivos de leitura somente leem, arquivos de escrita somente escreve
'''with open('novo.txt', 'w') as arquivo:
    arquivo.write(str(input('Digite algo: ') * 10))'''
with open('fruta.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe sua fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta + ' ')
        else:
            break
with open('fruta.txt') as arquivo:
    print(arquivo.read())