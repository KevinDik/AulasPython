''''
Utilizados para ler e criar arquivos em memoria
'''

from io import StringIO
mensagem = 'está é apenas uma string normal'

# pode criar arquivo em memoria ja co uma string inserida ou mesmo vazia para inserir texto depois

arquivo = StringIO(mensagem)

#agora com o arquivo, pode-se utilizar normalmente

print(arquivo.read())
arquivo.write('Outro texto')
arquivo.seek(0)
print(arquivo.read())
