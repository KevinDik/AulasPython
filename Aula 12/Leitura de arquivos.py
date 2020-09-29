arquivo = open('texto.txt')
print(arquivo)
print(type(arquivo))
#print(arquivo.read()) leitura do arquivo
#print(arquivo.read())
ret = arquivo.read() #mudança para string
print(type(ret))
print(ret)
