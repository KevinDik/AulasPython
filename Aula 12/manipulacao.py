'''
Sistema de manipulacao de arquivos

#criando arquivos
open('arquivo teste.txt', 'w').close()

open('arquivo teste2.txt', 'a').close()

with open('arquivo teste3.txt', 'w') as arquivo:
    pass

# saber se existe

# relativo
print(os.path.exists('arquivo.txt'))  # false

print(os.path.exists('geek'))  # true

print(os.path.exists('geek/univeristy'))  # true

print(os.path.exists('geek/outro'))  # false

# absoluto

print(os.path.exists('C:\\Users\\kevin\\Downloads'))

#linux
os.mknod('arquivo-teste4.txt')
os.mknod('C:\\arquivo.txt')

os.mkdir('templates') #cria se nao existir. caso nao fileexistserror. um a um

os.makedirs('templates/geek/univeristy') #cria varios diretorios em um comando

os.makedirs('templates2/novo2/outro2', exist_ok=True) #se apresentar erro. ignora

os.rename('templates2', 'geek2') #muda o nome. se o diretorio nap estiver vazio. tera os error
os.rename('geek2/novos', 'geek2/novo3')  # passar tudo para alterar

os.remove('arquivo teste.txt') #remove e nao vai para lixeira. se tiver em aberto, retorna em erro

import tempfile
#Arquivos temporarios criacao excecucao e destruicao
with tempfile.TemporaryDirectory() as temp:
    print(f'Criei o diretorio temporario em {temp}')
    with open(os.path.join(temp, 'arquivo-temporario.txt'), 'w') as arquivo:
        arquivo.write('geek univeristy')
    input()

import tempfile

with tempfile.TemporaryFile() as temp:
    temp.write(b'Geek university\n') #arquivos temps, so conseguem escrever bits
    temp.seek(0)
    print(temp.read())

sem o with
arquivo = tempfile.TemporaryFile()
arquivo.write('Geek')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
'''
import os
import tempfile

