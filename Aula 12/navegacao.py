import os

'''print(os.getcwd()) pega o current work directory. Diretorio do trabalho corrente

os.chdir('..') volta o diretorio
print(os.getcwd()) imprime o diretorio apos o retorno
print(os.path.isabs('home/geek/')) verifica se esta começando da raiz dos diretorios

computadores windows tem que ter cuidado ao verificar diretorios
print(os.path.isabs('C:\\Users\\geek'))

verifica qual sistema opercional posix ou nt
print(os.name)


import sys

print(sys.platform)

print(os.getcwd())
res = os.path.join(os.getcwd(), 'geek', 'univeristy') recebe doi parameros, 1 diretorio atual 2 o diretorio que sera juntadoao atual
os.chdir(res)
print(os.getcwd())

print(os.listdir())  #mostra o que tem dentro em formato de lista

print(list(os.scandir('C:\\'))) #scanner com mais detalhes
'''
#print(os.uname()) windows nao fornece
scanner = os.scandir()

arquivo = list(os.scandir())

print(arquivo[0].inode()) #endereco de memoria
print(arquivo[0].is_dir()) #é um diretorio
print(arquivo[0].is_file()) #é um arquivo
print(arquivo[0].is_symlink()) #é um linksimbolico
print(arquivo[0].path) #caminho ate o arquivo
print(arquivo[0].stat()) #??
print(arquivo[0].name)

scanner.close()