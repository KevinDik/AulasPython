from random import randint

numeros = [randint(1, 20) for valor in range(7)]
par = impar = 0
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

