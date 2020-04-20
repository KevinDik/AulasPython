from random import randint

numeros = []
par = impar = 0
for item in range(1, 7):
    numeros.append(randint(1, 20))
print('Numeros "Digitados"', numeros)
print()
print('Numeros pares digitados: ', end='')
for valor in numeros:
    if valor % 2 == 0:
        par += valor
        print(valor, end=' ')
print()
print('A soma dos valores pares digitados: ', par)
print()
print('Numeros impares digitados: ', end='')
for valor in numeros:
    if valor % 2 == 1:
        impar += valor
        print(valor, end=' ')
print()
print('a soma dos valores impares digitados: ', impar)

