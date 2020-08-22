lista = [1, 8, 4, 99, 34, 129]
print(type(lista))
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(type(tupla))
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(type(conjunto))
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(type(dicionario))
print(max(dicionario.values()))

print(max('Geek University'))

nomes = ['Arya', 'Sanson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "tunderstruck", "Tocou": 3},
    {"titulo": "dead skin mask", "Tocou": 200},
    {"titulo": "back in black", "Tocou": 4},
    {"titulo": "too old to rock in roll, too ynoung to die", "Tocou": 32}
]

print(max(musicas, key=lambda musica: musica["Tocou"]))
print(min(musicas, key=lambda musica: musica["Tocou"]))

print(max(musicas, key=lambda musica: musica["Tocou"])['titulo'])
print(min(musicas, key=lambda musica: musica["Tocou"])['titulo'])

maior = 0
for musica in musicas:
    if musica["Tocou"] > maior:
        maior = musica["Tocou"]
for musica in musicas:
    if musica['Tocou'] == maior:
        print(musica['titulo'])

maior = 10
for musica in musicas:
    if musica["Tocou"] < maior:
        maior = musica["Tocou"]
for musica in musicas:
    if musica['Tocou'] == maior:
        print(musica['titulo'])

#criar um sistema de nomes e organizar conforme letra
#Sistema de exememplo no uso das funcoes min e max


def funcaominmax(numero):
    from time import sleep
    if numero == 1:
        quantidade = int(input('Digite a quantidade de numeros: '))
        valor = [input('Digite um valor: ') for numero in range(quantidade)]
        print(f'Menor valor digitado é: {min(valor)}')
    elif numero == 2:
        quantidade = int(input('Digite a quantidade de numeros: '))
        valor = [input('Digite um valor: ') for numero in range(quantidade)]
        print(f'Maior valor digitado é: {max(valor)}')
    elif numero == 3:
        print('Saindo', end='')
        for c in range(3):
            print('.', end='')
            sleep(1)


while True:
    print('-' * 20)
    print('1: Minimo\n2: Maximo\n3: EXIT')
    print('-' * 20)
    opc = int(input('Escolha um item: '))
    funcaominmax(opc)
    if opc == 3:
        break
