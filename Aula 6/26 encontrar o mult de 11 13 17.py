print('Saber se um número é multiplo de 11 13 ou 17')
numero = int(input('Digite um número: '))
for c in range(1, 18):
    if numero / 11 == c or numero / 13 == c or numero / 17 == c:
        print(f'Número {numero} é multiplo de 11, 13 ou 17')
