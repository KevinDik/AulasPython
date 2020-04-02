n1 = int(input('Digite o prmeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = 0
mult = []
multiplicacao = 1
if n1 < n2:
    for c in range(n1, n2+1):
        if c % 2 == 0:
            soma += c
        elif c % 2 == 1:
            mult.append(c)

else:
    for c in range(n2, n1+1):
        if c % 2 == 0:
            soma += c
        elif c % 2 == 1:
            mult.append(c)
print(f'A soma dos valores entre {n1} e {n2} é de {soma}')
for c in mult:
    multiplicacao *= c
print(f'A multiplicação dos valores entre {n1} e {n2} é de {multiplicacao}')

