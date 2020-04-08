# 1 + 2 + 3 ... + n
# 1 - 2 + 3 - 4 ... + n (2n - 1)
# 1 + 3 + 5 + 7 + 9 ... + n (2n - 1)
numero = int(input('Digite um número: '))
somaSimples = somaAlternada = somaImpar = 0
for item in range(1, numero+1):
    somaSimples += item
    if item % 2 == 1:
        somaImpar += item
        somaAlternada += item
    if item % 2 == 0:
        somaAlternada -= item
print(f'A soma dos valores de 1 até {numero} é de {somaSimples}')
print(f'A soma dos sinais alternadas de 1 até {numero} é de {somaAlternada}')
print(f'A soma dos valores impares de 1 até {numero} é de {somaImpar}')

