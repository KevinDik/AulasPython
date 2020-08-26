def pegavalor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'nome': 'geek'}

print(pegavalor(dic, 'nome'))