# E = 1 + 1 / 1! + 1 / 2!...
valor = int(input('Digite um valor: '))
fatorial = []
e = 1
for c in range(1, valor+1):
    fatorial.append(c)
for c in fatorial:
    e = e + 1 / c
print(f'Para a formula E = 1 + 1 / 1!... De acordo com o valor informado {valor} o resultado é de {e}')
