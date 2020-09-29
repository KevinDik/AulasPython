with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


print(arquivo.closed)