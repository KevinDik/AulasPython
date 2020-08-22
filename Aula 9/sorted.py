numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))


print(sorted(numeros, reverse=True))

usuarios = [
    {"username": "samuel", "Tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "Tweets": ["Eu amo gato"]},
    {"username": "jeff", "Tweets": []},
    {"username": "bob", "Tweets": [], "cor": "amarelo"},
    {"username": "doggo", "Tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gol", "Tweets": [], "cor": "preto", "musica": "rock"}
]
print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

print(sorted(usuarios, key=lambda usuario: len(usuario["Tweets"])))

musicas = [
    {"titulo": "tunderstruck", "Tocou": 3},
    {"titulo": "dead skin mask", "Tocou": 2},
    {"titulo": "back in black", "Tocou": 4},
    {"titulo": "too old to rock in roll, too ynoung to die", "Tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica["Tocou"]))
print(sorted(musicas, key=lambda musica: musica["Tocou"], reverse=True))

