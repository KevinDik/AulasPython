listas = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
[[print(valor, end=' ') for valor in lista if valor % 2 == 0] for lista in listas]
print(listas)

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

velha = [['x' if numero % 2 == 0 else 'o' for numero in range(1, 4)] for campo in range(1, 4)]
print(velha)

numeros = {1, 2, 3, 4, 5}
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

chaves = 'abcd'
valores = [1, 2, 3, 4]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
