arquivo = open('texto.txt')
print(arquivo.read())
arquivo.seek(0) #movimenta o cursor para o inicio
#print(arquivo.readline()) #imprime uma linha
#print(arquivo.readline())
#ret = arquivo.readline()
#print(ret.split())
print(arquivo.readlines())
print(arquivo.closed) #verifica se esta fechado
arquivo.close() # fecha a conexao do arquivo
print(arquivo.closed)
arquivo.read()# apos o fechamento nao sera possivel manipular